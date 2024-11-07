import cv2
import os
import git

# 指定保存照片的路径
save_path = 'C:\\Users\\admin\\Desktop\\rep2_for github'
repo_path = save_path

if not os.path.exists(save_path):
    os.makedirs(save_path)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('Camera', frame)
    key = cv2.waitKey(1)
    if key == ord('p'):
        # 拍照并保存到指定路径，如有同名文件则覆盖
        photo = frame
        file_name = os.path.join(save_path, 'captured_photo.jpg')
        if os.path.exists(file_name):
            os.remove(file_name)
        cv2.imwrite(file_name, photo)
        break

cap.release()
cv2.destroyAllWindows()

import git

new_name = 'captured_photo.jpg'
repo_path = save_path

new_name = 'captured_photo.jpg'
repo = git.Repo(repo_path)

import subprocess

# 启动 Bash 脚本的方法
def run_bash_script(script_path):
    try:
        result = subprocess.run(['bash', script_path], capture_output=True, text=True)
        if result.returncode == 0:
            print("脚本执行成功。")
            print(result.stdout)
        else:
            print("脚本执行失败。")
            print(result.stderr)
    except Exception as e:
        print(f"发生错误：{e}")

# 调用示例
script_path = 'C:\Users\admin\Desktop\rep2_for github\git_push.sh'
run_bash_script(script_path)

