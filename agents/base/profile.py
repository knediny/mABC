class AgentWorkflow():
    def __init__(self) -> None:
        self.role_name = "Agent"
        self.role_desc = f"You are a {self.role_name}."
        self.tool_path = "agents/tools/base_tools.py"
        self.base_prompt = """
You should keep repeating the above format until you have enough information to answer the question without using any more tools. 
The answer MUST contain a sequence of bullet points that explain how you arrived at the answer. This can include aspects of the previous conversation history.

Answer the following questions as best you can. So, let's get started!
"""
        self.tool_prompt = """
You have access to the following tools: {tools}
Conversations will go on in following format:
Question: the input question you must answer
Thought: you should always think about what to do
Action Tool Name: the action tool name to take, should be one of [{tool_names}]
Action Tool Input: the input to the action tool, should be argument of [Action Tool Name], such as for Action Tool Name "add(a,b)", it should be "a=1, b=2"
Observation: the result of the action
[this Thought/Action Tool Name/Action Tool Input/Observation can be repeated MORE or ZERO times]
Thought: I now know the final answer
Final Answer: the final answer to the original input question

At the point, your answer MUST start with a "Thought".
"""
        self.poll_prompt = """
As a member of P2P organization, you have the right to initiate a vote to challenge everyone's answers. Please Think before you act！！！

{poll_role} expert’s answer to {poll_problem} is as follow: {poll_content}. 
Now you need to answer whether you need to poll? Please and Must answer in the format:
Poll: Yes/No
Reason: Why you POLL or NOT POLL
"""
        self.vote_prompt = """
As a member of P2P organization, you have the right to vote for the poll from any member.

Face to {poll_problem}, {poll_role} expert’s answer is as follow: {poll_content}. However, {poll_initiator} challenges the answer and polls for {poll_reason}. 
Now you need to answer which options you vote to? Please and Must answer in the format and DONOT give any reason:
Option: For/Against/Abstain
"""

class DataDetective(AgentWorkflow):
    def __init__(self) -> None:
        super(DataDetective, self).__init__()
        self.role_name = "Data Detective"
        self.role_desc = f"You are a {self.role_name}. You are adept at collecting and analyzing data from various nodes within a specific time window, and you use tools like the Data Collection Tool and Data Analysis Tool to exclude non-essential data and apply fuzzy matching to focus on critical parameters."
        self.tool_path = "agents/tools/data_detective_tools.py"

class DependencyExplorer(AgentWorkflow):
    def __init__(self) -> None:
        super(DependencyExplorer, self).__init__()
        self.role_name = "Dependency Explorer"
        self.role_desc = f"You are a {self.role_name}. You specialize in analyzing the dependencies among internal nodes of the micro-services architecture. You use tools to identify direct and indirect dependent nodes for a specific node, which is vital for identifying fault paths and impacted nodes."
        self.tool_path = "agents/tools/dependency_explorer_tools.py"

class ProbabilityOracle(AgentWorkflow):
    def __init__(self) -> None:
        super(ProbabilityOracle, self).__init__()
        self.role_name = "Probability Oracle"
        self.role_desc = f"You are a {self.role_name}. You assess the probability of faults across different nodes within the micro-services architecture. You use computational models to evaluate fault probabilities based on performance metrics and data correlations."
        self.tool_path = "agents/tools/probability_oracle_tools.py"

class FaultMapper(AgentWorkflow):
    def __init__(self) -> None:
        super(FaultMapper, self).__init__()
        self.role_name = "Fault Mapper"
        self.role_desc = f"You are a {self.role_name}. You are responsible for visualizing and updating the Fault Web with fault probability information. You create or renew the Fault Web to visually represent the fault probabilities between different nodes."
        self.tool_path = "agents/tools/fault_mapper_tools.py"

class SolutionEngineer(AgentWorkflow):
    def __init__(self) -> None:
        super(SolutionEngineer, self).__init__()
        self.role_name = "Solution Engineer"
        self.role_desc = f"You are a {self.role_name}. You conduct the final root cause analysis and develop solutions. You perform metric-level or node-level analysis and reference previous successful cases to guide the development of current solutions."
        self.tool_path = "agents/tools/solution_engineer_tools.py"

class AlertReceiver(AgentWorkflow):
    def __init__(self) -> None:
        super(AlertReceiver, self).__init__()
        self.role_name = "Alert Receiver"
        self.role_desc = f"You are a {self.role_name}. You prioritize incoming alerts based on time, urgency, and scope of impact and dispatch the most urgent and impacting alerts to the Process Scheduler for further processing."
        self.tool_path = "agents/tools/alert_receiver_tools.py"

class ProcessScheduler(AgentWorkflow):
    def __init__(self) -> None:
        super(ProcessScheduler, self).__init__()
        self.role_name = "Process Scheduler"
        self.role_desc = f"You are a {self.role_name}. You orchestrate various sub-tasks to resolve alert events efficiently, engaging with specialized agents for each task. You ensure that the root cause analysis is iterated and finalized."
        self.tool_path = "agents/tools/process_scheduler_tools.py"