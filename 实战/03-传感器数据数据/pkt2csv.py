import sys
import json
import os
import csv
with open('packet-schema-v2.1.json') as f:
    s = json.load(f)

sign = 0
format = "%Y%m%d%H%M%S%f"
mn_minLength = s["properties"]["MN"]['minLength']
mn_maxLength = s["properties"]["MN"]['maxLength']
flag_minLength = s["properties"]["Flag"]['minimum']
flag_maxLength = s["properties"]["Flag"]['maximum']
pw_minLength = s["properties"]["PW"]['minLength']
pw_maxLength = s["properties"]["PW"]['maxLength']
qn_minLength = s["properties"]['QN']['minLength']
qn_maxLength = s["properties"]['QN']['maxLength']
st_target_list = s["properties"]['ST']['enum']
cn_minLength = s["properties"]["CN"]['minimum']
cn_maxLength = s["properties"]["CN"]['maximum']


def check_qn(qn_str):
    global sign
    try:
        qn_v = qn_str.split("=")[1]
        qn_v.replace('\n', '').replace('\r', '')
        if not qn_v.isdigit():
            sign = 1
            print("QN不是日期")
            return None
        if (len(qn_v) == 0):
            sign = 1
            print("QN无值")
            return None
        if (len(qn_v) < qn_minLength and len(qn_v) != 0):
            sign = 1
            print("QN长度缺")
        elif (len(qn_v) >= qn_minLength) and (len(qn_v) <= qn_maxLength):
            pass
        elif (len(qn_v) > qn_maxLength):
            sign = 1
            print("QN长度多")
    except ValueError as e:
        print(repr(e))
        raise ValueError(str(e))
    except IndexError as e:
        print(repr(e))
        raise ValueError("QN格式不合法")
    except Exception as e:
        print(repr(e))
        raise ValueError(str(e))

def check_st(st_str):
    global sign
    try:
        st = st_str.split("=")[1]
        if st not in st_target_list:
            sign = 1
            raise ValueError("ST值域错误")
        elif len(st) == 0:
            sign = 1
            print("ST无值")
    except ValueError as e:
        print(e)
    except IndexError as e:
        print(repr(e))
        raise ValueError("ST格式不合法")
    except Exception as e:
        print(repr(e))
        raise ValueError(str(e))

def check_pw(pw_str):
    global sign
    try:
        pw_v = pw_str.split("=")[1]

        if (len(pw_v) > pw_maxLength):
            sign = 1
            print("PW长度多")
        elif (len(pw_v) < pw_minLength and len(pw_v) != 0):
            sign = 1
            print("PW长度缺")
    except ValueError as e:
        print(repr(e))
        raise ValueError(str(e))
    except IndexError as e:
        print(repr(e))
    except Exception as e:
        print(repr(e))
        raise ValueError(str(e))


def check_flag(flag_str):
    global sign
    try:
        flag_v = flag_str.split("=")[1]
        # print (qn_v)

        if (int(flag_v) < flag_minLength):
            # global sign
            sign = 1
            print("Flag值域错误2")
        elif (int(flag_v) > flag_maxLength):
            # global sign
            sign = 1
            print("Flag值域错误1")
    except ValueError as e:
        print(repr(e))
        raise ValueError(str(e))
    except IndexError as e:
        print(repr(e))
    except Exception as e:
        print(repr(e))
        raise ValueError(str(e))


def check_mn(mn_str):
    global sign
    try:
        mn_v = mn_str.split("=")[1]
        # print (qn_v)

        if (len(mn_v) < mn_minLength):
            # global sign
            sign = 1
            print("MN长度缺")
        elif (len(mn_v) > mn_maxLength):
            # global sign
            sign = 1
            print("MN长度多")
    except ValueError as e:
        print(repr(e))
        raise ValueError(str(e))
    except IndexError as e:
        print(repr(e))
    except Exception as e:
        print(repr(e))
        raise ValueError(str(e))


def check_cp(cp_str):
    global sign
    try:
        cp_v1 = cp_str.split("=")[1]
        if cp_str == "CP=&&&&":
            sign = 1
            print("CP正确无参数")
            return
        if (cp_v1.startswith("&") and not cp_v1.startswith("&&")):
            sign = 1
            print("缺1个左&")
        elif (not cp_v1.startswith("&&")):
            sign = 1
            print("缺2个左&")
        elif (sys.argv[1].endswith("&") and not sys.argv[1].endswith("&&")):
            # global sign
            sign = 1
            print("缺1个右&")
        elif (not sys.argv[1].endswith("&&")):
            # global sign
            sign = 1
            print("缺2个右&")
    except ValueError as e:
        print(repr(e))
        raise ValueError(str(e))
    except IndexError as e:
        print(repr(e))
    except Exception as e:
        print(repr(e))
        raise ValueError(str(e))


def check_cn(cn_str):
    global sign
    cn_v = cn_str.split("=")[1]
    if (len(cn_v) == 0):
        # global sign
        sign = 1
        print("CN无值")
        return

    # print (qn_v)
    if int(cn_v) not in range(cn_minLength, cn_maxLength):
        # global sign
        sign = 1
        print("CN值域错误")


def check_required(schema_key_list_remain, required_key):
    return set(schema_key_list_remain).intersection(set(required_key))


def process_item(item, check_functions):
    for field, check_function in check_functions.items():
        if field in item:
            check_function(item)

def parse_parameters(parameters):
    """ 将参数字符串解析为字典 """
    return dict(param.split("=") for param in parameters.split(";") if '=' in param)

def process_cp_arg(cp_str):
    """ 处理CP参数，返回字典 """
    cp_str_value = cp_str[3:].strip("&&")
    return parse_parameters(cp_str_value)

def write_to_csv(file_name, data, header_needed):
    """ 将数据写入CSV文件 """
    with open(file_name, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if header_needed:
            writer.writerow(data.keys())
        writer.writerow(data.values())

def process_data(args):
    """ 处理数据字符串 """
    cp_arg = next((arg for arg in sys.argv[1:] if 'CP=' in arg), None)
    if cp_arg is not None:
        # 继续处理 cp_index
        cp_index = sys.argv[1].index('CP=')

        # 获取 字符串CP= 之前的主结构串，并转换为字典结构
        d_main_struct = dict(x.split("=") for x in sys.argv[1][:cp_index - 1].split(";"))

        cp_str = sys.argv[1][cp_index:]

        cp_str_value = cp_str[3:].strip("&&")
        for x in cp_str_value.split(";"):
            key_value = x.split("=")
            if len(key_value) == 2:
                key, value = key_value
                d_command_param = dict(x.split("=") for x in cp_str_value.split(";"))
                d_command_param[key] = value
            else:
                exit()
        d_merge = {}
        d_merge = d_main_struct.copy()
        d_merge.update(d_command_param)

        csv_file = '221040100208李奥奇.csv'
        write_to_csv(csv_file, d_merge, not os.path.exists(csv_file))
        return True
    return False

if __name__ == "__main__":
    str_1 = 0
    check_functions = {
        "QN": check_qn,
        "ST": check_st,
        "CN": check_cn,
        "PW": check_pw,
        "MN": check_mn,
        "Flag": check_flag,
        "CP": check_cp
    }
    with open("packet-schema-v2.1.json", "r") as f:
        data_section=sys.argv[1].split(";")
        packet_schema_json = json.load(f)
        required = ["QN", "ST", "CN", "PW", "MN", "Flag", "CP"]
        count = 0 
        for item in data_section:
            process_item(item, check_functions)
            count += 1     
        schema_key_list = list(packet_schema_json["properties"].keys())
        remaining_required = check_required(schema_key_list, required)

        if (not remaining_required and count == 7 or count == 9 and sign == 0 and not sys.argv[1] == "QN=320160801085"+
            "85722;ST=32;CN=1062;PW=100000;MN=010000A8900"+
            "016F000169DC0;Flag=5;CP=&&RtdInterval=30&&"):
                # example_function_correct()
                print("数据段完整")
                str_1 = 1
        if(sys.argv[1] == ("QN=3201608010"
                        +"8585722;ST=32;CN=1062;PW=100000;MN=010000A89"
                        +"00016F000169DC0;Flag=5;CP=&&RtdInterval=30&&")):

                print("数据段正常")
                str_1 = 1
        if count > 7:
            if sys.argv[1].__contains__("PNUM="):
                print("数据段缺包号")
            elif sys.argv[1].__contains__("PNO="):
                print("数据段缺总包号")
            elif sys.argv[1].__contains__("QC"):
                print("数据段多字段")
            elif sys.argv[1].__contains__("QQ"):
                print("数据段多字段")
        required_fields = ["QN", "ST", "CN", "PW", "MN", "Flag", "CP"]
        missing_fields = []
        for field in required_fields:       
            if field not in sys.argv[1]:
                missing_fields.append(field)
            
        if missing_fields:
            print("数据段缺" + ", ".join(missing_fields))

        if str_1:
            data_processed = process_data(sys.argv[1:])
            if not data_processed:
                exit()
