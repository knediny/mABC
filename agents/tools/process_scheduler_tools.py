from agents.base.profile import (
    AgentWorkflow, DataDetective, DependencyExplorer, SolutionEngineer, 
    ProbabilityOracle, FaultMapper, AlertReceiver, ProcessScheduler
)
from agents.base.run import BaseRun, ReActTotRun, ThreeHotCotRun

# def ask_for_base_agent(question: str) -> str:
#     """
#     The Base Agent is the most basic agent in the system. It is the first agent to be called when a question is asked. The Base Agent just returns the answer with thinking.
    
#     Parameters:
#     - question (str): The question to ask the Base Agent, you should describe the problem in detail as much as possible, because Base Agent do not know anything about the question.

#     Returns:
#     - str: The response from the Base Agent.
#     """
#     base_agent = BaseAgent()
#     run = BaseRun()
#     return run.run(base_agent, question)

def ask_for_data_detective(question: str) -> str:
    """
    Ask for Data Detective Agent about endpoint metric in a endpoint. Data Detective Agent monitors and analyzes endpoint metric using functions like query_endpoint_metrics_in_range(endpoint, time). The endpoint metrics, including API call count, success rate, error rate, response time and timeout rate, are used to identify trends and issues in this endpoint.
    
    Parameters:
    - question (str): The question to ask the Data Detective Agent, you should describe the question in detail as much as possible including Endpoint and Time, because Data Detective Agent only know what you have told it.

    Returns:
    - str: The response from the Data Detective Agent.
    """
    data_detective = DataDetective()
    run = ReActTotRun()
    eval_run = ThreeHotCotRun()
    agents = [DataDetective(), DependencyExplorer(), SolutionEngineer(), ProbabilityOracle(), FaultMapper(), AlertReceiver(), ProcessScheduler()]
    from agents.tools import data_detective_tools
    return run.run(data_detective, question, vars(data_detective_tools), eval_run, agents)


def ask_for_dependency_explorer(question: str) -> str:
    """
    Ask for Dependency Explorer Agent about trace. Dependency Explorer Agent manages and analyzes endpoint relationships within a microservice system's architecture. They utilize functions to track downstream endpoints for a endpoint and a specific time like get_downstream(endpoint, time) to aid in helping you understand system workflows.

    Parameters:
    - question (str): The question to ask the Dependency Explorer Agent, you should describe the question in detail as much as possible including Endpoint and Time, because Dependency Explorer Agent only know what you have told it.

    Returns:
    - str: The response from the Dependency Explorer Agent.
    """
    denpendency_explorer = DependencyExplorer()
    run = ReActTotRun()
    eval_run = ThreeHotCotRun()
    agents = [DataDetective(), DependencyExplorer(), SolutionEngineer(), ProbabilityOracle(), FaultMapper(), AlertReceiver(), ProcessScheduler()]
    from agents.tools import denpendency_explorer_tools
    return run.run(denpendency_explorer, question, vars(denpendency_explorer_tools), eval_run, agents)

def ask_for_solution_engineer(question: str) -> str:
    """
    The Solution Engineer Agent is responsible for providing solutions by analyzing the root causes of issues within the API ecosystem. They use functions like conduct_root_cause_analysis and develop_solution to propose and track the status of solutions, as well as to understand their impact on the system.

    Parameters:
    - question (str): The question for the Solution Engineer Agent should include detailed information about the current situation and the problem at hand.

    Returns:
    - str: The response from the Solution Engineer Agent.
    """
    solution_engineer = SolutionEngineer()
    run = ReActTotRun()
    eval_run = ThreeHotCotRun()
    agents = [DataDetective(), DependencyExplorer(), SolutionEngineer(), ProbabilityOracle(), FaultMapper(), AlertReceiver(), ProcessScheduler()]
    from agents.tools import solution_engineer_tools
    return run.run(solution_engineer, question, vars(solution_engineer_tools), eval_run, agents)

def ask_for_probability_oracle(question: str) -> str:
    """
    The Probability Oracle Agent evaluates the likelihood of faults across different nodes within the micro-services architecture. It uses computational models to determine fault probabilities based on performance metrics and data correlations.

    Parameters:
    - question (str): The question for the Probability Oracle Agent should include detailed information about the nodes in question.

    Returns:
    - str: The response from the Probability Oracle Agent.
    """
    probability_oracle = ProbabilityOracle()
    run = ReActTotRun()
    eval_run = ThreeHotCotRun()
    agents = [DataDetective(), DependencyExplorer(), SolutionEngineer(), ProbabilityOracle(), FaultMapper(), AlertReceiver(), ProcessScheduler()]
    from agents.tools import probability_oracle_tools
    return run.run(probability_oracle, question, vars(probability_oracle_tools), eval_run, agents)

def ask_for_fault_mapper(question: str) -> str:
    """
    The Fault Mapper Agent is responsible for visualizing the fault web within the micro-services architecture. It updates the fault web with the latest fault probability information to assist in identifying the root causes of issues.

    Parameters:
    - question (str): The question for the Fault Mapper Agent should include detailed information about the fault probabilities and nodes in question.

    Returns:
    - str: The response from the Fault Mapper Agent.
    """
    fault_mapper = FaultMapper()
    run = ReActTotRun()
    eval_run = ThreeHotCotRun()
    agents = [DataDetective(), DependencyExplorer(), SolutionEngineer(), ProbabilityOracle(), FaultMapper(), AlertReceiver(), ProcessScheduler()]
    from agents.tools import fault_mapper_tools
    return run.run(fault_mapper, question, vars(fault_mapper_tools), eval_run, agents)

# def ask_for_alert_receiver(question: str) -> str:
#     """
#     The Alert Receiver Agent is responsible for prioritizing incoming alerts based on their urgency and potential impact. It sorts alerts to ensure that the most critical ones are addressed promptly.

#     Parameters:
#     - question (str): The question for the Alert Receiver Agent should include detailed information about the incoming alerts.

#     Returns:
#     - str: The response from the Alert Receiver Agent.
#     """
#     alert_receiver = AlertReceiver()
#     run = ReActTotRun()
#     eval_run = ThreeHotCotRun()
#     agents = [DataDetective(), DependencyExplorer(), SolutionEngineer(), ProbabilityOracle(), FaultMapper(), AlertReceiver(), ProcessScheduler()]
#     from agents.tools import alert_receiver_tools
#     return run.run(alert_receiver, question, vars(alert_receiver_tools), eval_run, agents)

# def ask_for_process_scheduler(question: str) -> str:
#     """
#     The Process Scheduler Agent orchestrates the tasks across different agents to ensure efficient resolution of alert events. It delegates sub-tasks to specialized agents and ensures the root cause analysis is iterated and finalized.

#     Parameters:
#     - question (str): The question for the Process Scheduler Agent should include detailed information about the alert events and the required sub-tasks.

#     Returns:
#     - str: The response from the Process Scheduler Agent.
#     """
#     process_scheduler = ProcessScheduler()
#     run = ReActTotRun()
#     eval_run = ThreeHotCotRun()
#     agents = [DataDetective(), DependencyExplorer(), SolutionEngineer(), ProbabilityOracle(), FaultMapper(), AlertReceiver(), ProcessScheduler()]
#     from agents.tools import process_scheduler_tools
#     return run.run(process_scheduler, question, vars(process_scheduler_tools), eval_run, agents)