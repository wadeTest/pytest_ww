import subprocess
import time


class AdbLogcatHelper:
    @staticmethod
    def run_shell_command(command):
        try:
            # 使用 subprocess.Popen 执行命令
            process = subprocess.Popen(
                command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )

            # 获取命令的标准输出和标准错误输出
            output, error = process.communicate()

            # 解码输出为 utf-8 编码
            output = output.decode("utf-8")
            error = error.decode("utf-8")

            # 返回输出结果
            return output.strip(), error.strip()
        except Exception as e:
            # 捕获命令执行错误
            return None, str(e)

    @staticmethod
    def restart_server():
        """
        重啟 ADB 服務器。
        """
        try:
            # 执行 adb kill-server 命令
            kill_output, kill_error = AdbLogcatHelper.run_shell_command(
                "adb kill-server"
            )
            if kill_error:
                print("Error killing ADB server:", kill_error)
                return

            # 执行 adb start-server 命令
            start_output, start_error = AdbLogcatHelper.run_shell_command(
                "adb start-server"
            )
            if start_error:
                print("Error starting ADB server:", start_error)
                return

            print("ADB server restarted successfully.")
        except Exception as e:
            print("Error restarting ADB server:", e)

    @staticmethod
    def get_adb_sms_msg():
        """
        取得手機內簡訊
        """
        adb_command = "adb shell content query --uri content://sms/"
        output, error = AdbLogcatHelper.run_shell_command(adb_command)
        if error:
            print("攔截簡訊失敗：", error)
            return None
        else:
            return output

    def find_latest_sms(self, data):
        content = data
        split_data = content.split(
            "protocol=0, read=1, status=-1, type=1, reply_path_present=0, subject=NULL, body=【無敵娛樂王】"
        )

        msg_data_replace = [
            item.replace(
                "locked=0, sub_id=1, error_code=0, creator=com.google.android.apps.messaging, seen=1\r\n",
                "",
            )
            for item in split_data
        ]

        # print(msg_data_replace)
        concat_log = "".join(msg_data_replace)
        raw_rows = concat_log.split("Row:")
        rows = ["Row:" + row.strip() for row in raw_rows if row]
        result = rows[0].split("【無敵娛樂王】驗證碼：")[1].split("。")[0]
        print(result)
        return result


if __name__ == "__main__":
    adb_helper = AdbLogcatHelper()
    print("重啟ADB...")
    adb_helper.restart_server()
    time.sleep(1)
    print("正在取得手機簡訊...")
    sms_msg = adb_helper.get_adb_sms_msg()
    if sms_msg:
        result = AdbLogcatHelper().find_latest_sms(sms_msg)
