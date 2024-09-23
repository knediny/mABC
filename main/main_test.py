from agents.base.profile import DataDetective, DependencyExplorer, ProbabilityOracle, FaultMapper, AlertReceiver, ProcessScheduler, SolutionEngineer
from agents.base.run import ReActTotRun, ThreeHotCotRun, BaseRun
from agents.tools import process_scheduler_tools, alert_receiver_tools, solution_engineer_tools
import json

if __name__ == "__main__":
    questions = ["16 + 23 * 44 + 99 / 9 = ?", "1 - 9 + 2 * 16 + 99 / 9 * 8 + 7 - 6 = ?"]

    for question in questions:
        agent = ProcessScheduler()
        run = ReActTotRun()
        eval_run = ThreeHotCotRun(alpha=0, beta=0)
        agents = [DataDetective(), DependencyExplorer(), ProbabilityOracle(), FaultMapper(), AlertReceiver(), ProcessScheduler(), SolutionEngineer()]
        answer = run.run(agent=agent, question=question, agent_tool_env=vars(process_scheduler_tools), eval_run=eval_run, agents=agents)
        print(answer)

