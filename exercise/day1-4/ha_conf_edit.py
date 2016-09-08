import json, os, string

'''
Get matching "backend_title" following records
'''
def fetch(backend):
    backend_title = 'backend %s' % backend
    record_list = []
    with open('ha.conf','r') as file:
        flag = False
        for line in file:
            line = line.strip()
            if line == backend_title:
                flag = True
                continue
            if flag and line.startswith('backend'):
                flag = False
                break
            if flag and line:
                record_list.append(line)
    return record_list#若文件中含有此字段则返回字段下的记录, 若不存在则返回空list

#print(fetch('test.oldboy.org'))

def add(dict_info):
    backend = dict_info.get('backend')
    record_list = fetch(backend)
    backend_title = 'backend %s' % backend
    #current_record 保存的是修改后的记录
    current_record = 'server %s %s weight %d maxconn %d' % (dict_info['record']['server'], dict_info['record']['server'], dict_info['record']['weight'], dict_info['record']['maxconn'])
    if not record_list:#没有这个backend 时的处理
        record_list.append(backend_title)
        record_list.append(current_record)
        with open('ha.conf') as read_file, open('ha.new','w') as write_file:

            for line in read_file:
                write_file.write(line)
            for i in record_list:
                if i.startswith('backend'):
                    write_file.write(i+'\n')
                else:
                    write_file.write('%s%s\n' % (8*' ',i))
    else:#配置文件中包含有这个backend 字段
        record_list.insert(0,backend_title)#取出的记录不包含以backend 开头的字段, 需要insert
        if current_record not in record_list:
            record_list.append(current_record)
        with open('ha.conf') as read_file, open('ha.new','w') as write_file:
            flag = False
            has_write = False
            for line in read_file:
                line_strip = line.strip()
                if line_strip == backend_title:
                    flag = True
                    continue
                if flag and line_strip.startswith('backend'):
                    flag = False
                if not flag:
                    write_file.write(line)
                else:
                    if not has_write:
                        for i in record_list:
                            print(i)
                            if i.startswith('backend'):
                                write_file.write(i+'\n')
                            else:
                                write_file.write('%s%s\n' % (8*' ',i))
                    has_write = True
    os.rename('ha.conf','ha.conf.back')
    os.rename('ha.new','ha.conf')

def remove(dict_info):
    backend = dict_info.get('backend')
    record_list = fetch(backend)
    backend_title = "backend %s" % backend
    current_record = "server %s %s weight %d maxconn %d" % (dict_info['record']['server'], dict_info['record']['server'], dict_info['record']['weight'], dict_info['record']['maxconn'])
    if not record_list:
        return
    else:
        if current_record not in record_list:
            return
        else:
            del record_list[record_list.index(current_record)]
            record_list.insert(0,backend_title)
        with open('ha.conf') as read_file, open('ha.new', 'w') as write_file:
            flag = False
            has_write = False
            for line in read_file:
                line_strip = line.strip()
                if line_strip == backend_title:
                    flag = True
                    continue
                if flag and line_strip.startswith('backend'):
                    flag = False
                if not flag:
                    write_file.write(line)
                else:
                    if not has_write:
                        for i in record_list:
                            if i.startswith('backend'):
                                write_file.write(i+'\n')
                            else:
                                write_file.write('%s%s\n' % (8*' ',i))
                    has_write = True
    os.rename('ha.conf','ha.conf.back')
    os.rename('ha.new','ha.conf')

if __name__ == '__main__':

    print('1、获取；2、添加；3、删除')
    num = input('请输入序号：')
    data = input('请输入内容：')
    #print(num,data)
    if num == '1':
        fetch(data)
    else:
        dict_data = json.loads(data)
        if num == '2':
            add(dict_data)
        elif num == '3':
            remove(dict_data)
        else:
            pass