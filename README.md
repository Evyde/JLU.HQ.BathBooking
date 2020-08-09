# jlu-bath-booking

吉林大学预订浴池脚本

## 使用方法

### Requirements

```
python (本项目使用python版本为3.7.6)
selenium
```

### 下载脚本

```
git clone git@github.com:TobisLee/jlu-bath-booking.git
cd jlu-bath-booking
```

### 添加student.json

```
根据student-example.json来建立student.json

name: 姓名
phone: 电话号
id: 学号
sex: 性别（男生填1，女生填2）
time: 要预约的洗澡时间（从1开始计数，例如11:00-11:45就填1，19:30-20:15就填12）
```

### 运行脚本

```
# 预订
python bath-booking.py
# 查询
python bath-check.py
```

