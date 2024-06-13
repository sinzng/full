from openai import OpenAI

client = OpenAI()

# 모든 파인튜닝 작업 목록 가져오기
fine_tunes = client.fine_tuning.jobs.list()

for fine_tune in fine_tunes.data:
    if fine_tune.status == "running":
        print(f'failed fine-tunning job:{fine_tune.id}')
        fine_tuning_event_job_id = fine_tune.id
response = client.fine_tuning.jobs.list_events(fine_tuning_event_job_id)
print(response)