import os
import sys
BASE_PATH = os.path.dirname(os.path.dirname(__file__))

# # 只存账号
# user_path = r'E:\PYXUEXI\OBPY1\005_def\user.txt'
# # 存账号和密码
# user_path_np = r'E:\PYXUEXI\OBPY1\005_def\user_np.txt'

user_path = os.path.join(BASE_PATH,'db','user.txt')
user_path_np = os.path.join(BASE_PATH,'db','user_np.txt')