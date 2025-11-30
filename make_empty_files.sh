#!/usr/bin/env bash
set -euo pipefail

# lessons 폴더 생성 및 이동
mkdir -p lessons && cd lessons

# 내용에 사용할 변수들을 정의
LINE1='import utils'
LINE2=''
LINE3='utils.show_base_name(__file__, True)'
LINE4=''
LINE5='def main() -> None:'
LINE6='    user_name = "World"'
LINE7='    print(utils.greet(user_name))'
LINE8='    # Demonstrate emoji utility'
LINE9='    print("Random emojis:", end=" ")'
LINE10='    utils.show_random_emojis(5)'
LINE11=''
LINE12='    utils.show_base_name(__file__, False)'
LINE13=''
LINE14='if __name__ == "__main__":'
LINE15='    main()'
LINE16='else:'
LINE17='    utils.show_base_name(__file__, False)'


# lesson01.sh부터 lesson31.sh까지 파일 생성 및 내용 채우기
for i in $(seq 1 31)
do
    # 숫자를 두 자리로 포맷팅
    filename="lesson$(printf "%02d" $i).py"

    # 파일이 존재하지 않는 경우에만 생성
    if [ ! -f "$filename" ]; then
        echo "💡 $filename 파일이 존재하지 않으므로 생성합니다."
        echo "$LINE1" >> "$filename"
        echo "$LINE2" >> "$filename"
        echo "$LINE3" >> "$filename"
        echo "$LINE4" >> "$filename"
        echo "$LINE5" >> "$filename"
        echo "$LINE6" >> "$filename"
        echo "$LINE7" >> "$filename"
        echo "$LINE8" >> "$filename"
        echo "$LINE9" >> "$filename"
        echo "$LINE10" >> "$filename"
        echo "$LINE11" >> "$filename"
        echo "$LINE12" >> "$filename"
        echo "$LINE13" >> "$filename"
        echo "$LINE14" >> "$filename"
        echo "$LINE15" >> "$filename"
        echo "$LINE16" >> "$filename"
        echo "$LINE17" >> "$filename"
    else
        echo "$filename 파일이 이미 존재합니다. 생성을 건너뜁니다."
    fi
done

echo "lessons 폴더와 lesson01.sh ~ lesson30.sh 파일 생성이 완료되었습니다."