from datetime import date
import glob
import fnmatch
import string
from pyvi import ViUtils

EMAIL_INFO = {
    "host": "mail.aiacademy.edu.vn",
    "email": "mptla@aiacademy.edu.vn",
    "password": "Alexa@Siri",
}
# DATABASE_INFO = {
#     "host": "128.199.194.183",
#     "database": "mp_tla_prod",
#     "user": "tla_developer",
#     "password": "mp_tla",
#     "port": 5432,
# }
DATABASE_INFO = {
    "host": "128.199.194.183",
    "database": "mp_tla",
    "user": "tla_developer",
    "password": "mp_tla",
    "port": 5432,
}
SAlE_MAIL_LIST = ["quangson@minhphu.com", "vanlen@minhphu.com"]
MANAGER_MAIL_LIST = [
    "ducchuc@minhphu.com",
    "thuynga@minhphu.com",
    "viettrung@minhphu.com",
    "hanguyen@minhphu.com",
]
OPERATOR_MAIL_LIST = ["xuannhi@minhphu.com", "hoangso8000@gmail.com"]
MESSAGE_INFO = {
    "subject": "Nhắc lịch đơn hàng",
    "body": "Chào bạn {},\nGửi bạn nhắc lịch được đính kèm trong các file dưới đây\nThân chào!",
}
EMPLOYEE_INFO = {
    "VŨ VĂN KHƯƠNG": "vukhuong@minhphu.com",
    "ĐẶNG QUANG SƠN": "quangson@minhphu.com",
    "NGÔ THỊ BỬU HƯỜNG": "huongngo@minhphu.com",
    "TRẦN ĐĂNG KHOA": "khoatran@minhphu.com",
    "TRẦN VĂN LEN": "vanlen@minhphu.com",
}
import re
import base64, quopri
import os


def encoded_words_to_text(encoded_words):
    encoded_word_regex = r"=\?{1}(.+)\?{1}([B|Q])\?{1}(.+)\?{1}="
    charset, encoding, encoded_text = re.match(
        encoded_word_regex, encoded_words
    ).groups()
    if encoding is "B":
        byte_string = base64.b64decode(encoded_text)
    elif encoding is "Q":
        byte_string = quopri.decodestring(encoded_text)
    return byte_string.decode(charset)


def createDirectory(directory):
    if not os.path.isdir(directory):
        os.makedirs(directory, exist_ok=True)

# tìm file theo regex
def findfiles(which, where="."):
    """Returns list of filenames from `where` path matched by 'which'
    shell pattern. Matching is case-insensitive."""

    # TODO: recursive param with walk() filtering
    rule = re.compile(fnmatch.translate(which), re.IGNORECASE)
    return [where + "/" + name for name in os.listdir(where) if rule.match(name)]


def no_accent_vietnamese(s):
    s = re.sub(r"[àáạảãâầấậẩẫăằắặẳẵ]", "a", s)
    s = re.sub(r"[ÀÁẠẢÃĂẰẮẶẲẴÂẦẤẬẨẪ]", "A", s)
    s = re.sub(r"[èéẹẻẽêềếệểễ]", "e", s)
    s = re.sub(r"[ÈÉẸẺẼÊỀẾỆỂỄ]", "E", s)
    s = re.sub(r"[òóọỏõôồốộổỗơờớợởỡ]", "o", s)
    s = re.sub(r"[ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ]", "O", s)
    s = re.sub(r"[ìíịỉĩ]", "i", s)
    s = re.sub(r"[ÌÍỊỈĨ]", "I", s)
    s = re.sub(r"[ùúụủũưừứựửữ]", "u", s)
    s = re.sub(r"[ƯỪỨỰỬỮÙÚỤỦŨ]", "U", s)
    s = re.sub(r"[ỳýỵỷỹ]", "y", s)
    s = re.sub(r"[ỲÝỴỶỸ]", "Y", s)
    s = re.sub(r"[Đ]", "D", s)
    s = re.sub(r"[đ]", "d", s)
    return s


def processColumn(df):
    df.columns = [
        no_accent_vietnamese(
            column.strip()
            .replace("(", "")
            .replace(")", "")
            .replace(" ", "_")
            .replace("/", "")
            .replace(".", "")
            .replace("__", "_")
        )
        for column in df.columns
    ]
    df.columns = [column.lower() for column in df.columns]
    return df


def remove_punct(test_str):
    for i in string.punctuation:
        if i in test_str:
            test_str = test_str.replace(i, " ")
    return test_str


def preprocess(a):
    a = " ".join(remove_punct(a).split())
    a = " ".join(a.lower().split())
    a = ViUtils.remove_accents(a)
    a = a.decode()
    a = " ".join(a.lower().split())
    a = a.replace(" ", "_")
    return a


def get_product_type(a):
    a = a.split()
    return a[0]


def get_process_type(a):
    a = a.split()
    return a[1]


def get_size(a):
    a = a.split()
    try:
        return a[2]
    except:
        print(a)
        pass


# def get_attachment(mail):

#     # attachment = mail.(mails)
#     download_path = f"{download_folder}/{filename}"
#     print(download_path)

#     with open(download_path, "wb") as fp:
#         fp.write(filecontent)
if __name__ == "__main__":
    # test = encoded_words_to_text(
    #     "=?utf-8?B?MDEgU+G7kSBsaeG7h3UgeHXhuqV0IG5o4bqtcCB04buTbi5YTFNY?="
    # )
    # print(test)
    # test1 = encoded_words_to_text(
    #     "=?UTF-8?B?MDIgQsOhbyBjw6FvIHRow6BuaCBwaOG6qW0gc+G6o24geHXhuqV0Llg=?="
    # )
    # print(test1)
    print( findfiles(f"NGÔ THỊ BỬU HƯỜNG-*.xlsx", f"output/2020-11-06")
    )
    
    print(preprocess("Nhà máy(Plant)"))
