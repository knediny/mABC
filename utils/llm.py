from settings import OPENAI_API_KEY, OPENAI_MAX_RETRIES, OPENAI_RETRY_SLEEP, OPENAI_MODEL
from openai import OpenAI
import time

def llm_chat(shared_messages, stop_words):
    for i in range(OPENAI_MAX_RETRIES):
        try:
            client = OpenAI(
                api_key=OPENAI_API_KEY,
            )
            completion = client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=shared_messages,
                stop=stop_words,
                # max_tokens=4096,
            )
            print(completion)
            return completion.choices[0].message.content
            # print(completion)
            # ChatCompletion(id='chatcmpl-8wLgj8eDyWI0BblpyfmveTH7xfVAg', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content="In the realm of code, a concept profound,\nRecursion's power shall astound.\nLike a mirror reflecting endless views,\nIt beckons us to see anew.\n\nA function calling itself, so bold,\nUnraveling mysteries, untold.\nThrough layers deep, it journeys on,\nUntil a base case is finally drawn.\n\nA loop unending, a cycle profound,\nInfinite patterns it can expound.\nLike the ripples in a tranquil pond,\nRecursive calls echo far beyond.\n\nYet heed with care, for a tale of warning,\nStacks may grow, memory adorning.\nWith elegance and grace, it plays its part,\nRecursion, a masterpiece of the programming art.\n\nSo embrace this concept, with vigor and might,\nFor in its depths, lies wisdom's light.\nA dance of logic, a symphony grand,\nRecursion, a marvel at our command.", role='assistant', function_call=None, tool_calls=None))], created=1708917085, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_86156a94a0', usage=CompletionUsage(completion_tokens=177, prompt_tokens=55, total_tokens=232))
        except Exception as e:
            print(e)
            time.sleep(OPENAI_RETRY_SLEEP)
            continue
    return "Connection error."

if __name__ == "__main__":
    shared_messages = [
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    ]
    shared_messages.append({"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."})
    answer = llm_chat(shared_messages, "")
    shared_messages.append({"role": "assistant", "content": answer})
    # print("*" * 100)
    # print(shared_messages)
    # print(f"Q: {question}\nA: {answer}")
    # print("*" * 100)
    print(shared_messages, answer)

