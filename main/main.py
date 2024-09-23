
from agents.base.profile import DataDetective, DependencyExplorer, ProbabilityOracle, FaultMapper, AlertReceiver, ProcessScheduler, SolutionEngineer
from agents.base.run import ReActTotRun, ThreeHotCotRun, BaseRun
from agents.tools import process_scheduler_tools, alert_receiver_tools, solution_engineer_tools
import json

if __name__ == "__main__":
    # question = "16 + 23 * 44 + 99 / 9 = ?"
    # question = "1 - 9 + 2 * 16 + 99 / 9 * 8 + 7 - 6 = ?"
    # T = "2024-01-09 09:00:00"
    # ENDPOINT = "ts-travel-plan-service-/api/v1/routeplanservice/routePlan/quickestRoute"
    i = 0
    with(open("data/label/label.json", "r")) as f:
        data = json.load(f)
    for t, v in data.items():
        for endpoint, path in v.items():
            print("@" * 30, "Decision Maker", "@" * 30)
            question = f"""Backgroud: In a distributed microservices system, there is a lot of traces across endpoints which represent the dependency relationship between endpoints. A trace consists of a sequence of spans, each representing a call from one endpoint to another when ignore the service level. 

            Alert generally occurs on the top endpoint at time T for a significant anomaly when the root cause endpoint at time T' is the downstream endpoint of the alerting endpoint. Endpoint A(TA) -> Endpoint B(TB) -> Endpoint C(TC) -> Endpoint D(TD), if the alert occurs on the Endpoint A at time TA, the root cause endpoint is the Endpoint C at time TC when the metric of Endpoint C is abnormal but the metric of Endpoint D at time TD is normal.

            Alert: Endpoint {endpoint} experiencing a significant increase in response time {t}. 
            Task: Please find the root cause endpoint behind the alerting endpoint {endpoint} by analyzing the metric of endpoint and the call trace. 
            Format: Root Cause Endpoint: XXX, Root Cause Reason: XXX
            """
            print(f"Q: {question}")
            # sort
            # answer = ReActTotRun.run(agent=AlertReceiver(), question=question, agent_tool_env=vars(alert_receiver_tools))
            agent = ProcessScheduler()
            run = ReActTotRun()
            eval_run = ThreeHotCotRun(0, 0)
            agents = [DataDetective(), DependencyExplorer(), ProbabilityOracle(), FaultMapper(), AlertReceiver(), ProcessScheduler(), SolutionEngineer()]
            answer = run.run(agent=agent, question=question, agent_tool_env=vars(process_scheduler_tools), eval_run=eval_run, agents=agents)
            print(f"A: {answer}")
            question = "Base on the analysis, what is the root cause endpoint?\n\n Format: Root Cause Endpoint: XXX, Root Cause Reason: XXX\n\n" + answer
            print(f"Q: {question}")
            # answer = BaseRun().run(agent=SolutionEngineer(), question=question, agent_tool_env=vars(solution_engineer_tools))
            agent = SolutionEngineer()
            agents = [SolutionEngineer()]
            answer = ReActTotRun().run(agent=agent, question=question, agent_tool_env=vars(solution_engineer_tools), eval_run=ThreeHotCotRun(), agents=agents)
            print(f"A: {answer}")
            print("@" * 30, "Solution Engineer", "@" * 30)
            print("\n" * 20)
            
            i += 1
            if i >= 5 :
                break
