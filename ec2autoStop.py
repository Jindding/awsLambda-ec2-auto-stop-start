# -*- coding: utf-8 -*-
import boto3
from datetime import datetime

# 서울 리전
region = 'ap-northeast-2'
# 월 ~ 일요일
t = ["월", "화", "수", "목", "금", "토", "일"]
# ec2-stop-start Access Key
ACCESS_KEY = 'Enter Your Access Key'
SECRET_KEY = 'Enter Your Secret Key'

def lambda_handler(event, context):
    # 람다 호출된시점의 시간 계산
    print("ec2 auto stop/start Lambda Start")
    now_date = t[datetime.today().weekday()]
    now_hour = int(datetime.now().strftime('%H')) + 9 # 로컬에서는 안맞을 수 있음
    print("now >> date: " + now_date + ", hour: " + str(now_hour))

    # ec2 인스턴스의 모든 태그 조회
    ec2 = boto3.client(
        'ec2',
        region_name=region,
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY
    )
    response = ec2.describe_tags(
        Filters=[
            {
                'Name': 'resource-type',
                'Values': ['instance']
            }
        ]
    )

    # 값 임시 저장
    enable_instances = []
    day_instances = {}
    time_instances = {}

    for tag in response['Tags']:
        if tag['Key'] == "AUTO_STOP_ENABLE" and tag['Value'].lower() == "true":
            enable_instances.append(tag['ResourceId'])
        if tag['Key'] == "AUTO_STOP_DAY":
            day_instances[tag['ResourceId']] = tag['Value']
        if tag['Key'] == "AUTO_STOP_TIME":
            time_instances[tag['ResourceId']] = tag['Value']

    for instance in enable_instances:
        try:
            # 요일 확인
            days = day_instances[instance].split(",")
            is_day = False
            for d in days:
                if now_date == d:
                    is_day = True

            # 시간 확인
            times = time_instances[instance].split("~")
            is_start_time = False
            is_end_time = False
            if int(times[1].strip()) == now_hour:
                is_end_time = True
            elif int(times[0].strip()) == now_hour:
                is_start_time = True

            if is_day == True and is_end_time == True:
                # 중지 인스턴스 호출
                ec2.stop_instances(InstanceIds=[instance])
                print('인스턴스 종료', [instance])
            elif is_day == True and is_start_time == True:
                # 시작 인스턴스 호출
                ec2.start_instances(InstanceIds=[instance])
                print('인스턴스 시작', [instance])
        except Exception as ex:
            print(ex)