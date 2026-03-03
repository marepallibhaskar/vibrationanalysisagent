import yaml, importlib

class Orchestrator:
    def __init__(self, agents_file, tools_file, tasks_file, pipeline_file):
        self.agents = yaml.safe_load(open(agents_file))["agents"]
        self.tools = yaml.safe_load(open(tools_file))["tools"]
        self.tasks = yaml.safe_load(open(tasks_file))["tasks"]
        self.pipeline = yaml.safe_load(open(pipeline_file))["pipeline"]
        self.memory = {"short_term": {}, "long_term": []}
        self.agent_instances = {}

    def instantiate_agents(self):
        for agent in self.agents:
            name = agent["name"]
            module = f"crew.{name.lower()}"
            cls = getattr(importlib.import_module(module), name)
            self.agent_instances[name] = cls()

    def run_task(self, task_id, context):
        task = next(t for t in self.tasks if t["id"] == task_id)
        agent = self.agent_instances[task["agent"]]
        tool_method = getattr(agent, task["tool"].lower())
        input_data = {k: context[k] for k in task.get("input", []) if k in context}
        output = tool_method(**input_data)
        context[task["output"]] = output
        self.memory["short_term"][task["output"]] = output
        return context

    def run_pipeline(self, context, query=None):
        self.instantiate_agents()
        for step in self.pipeline["steps"]:
            context = self.run_task(step["task"], context)

        self.memory["long_term"].append(self.memory["short_term"])

        if query:
            return self.agent_instances["MemoryAgent"].query_history(query)

        return context

