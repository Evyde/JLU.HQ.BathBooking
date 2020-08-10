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
bathID: 要预约的浴池地点（1 南区浴池，2 大学城，3 南岭，4 南湖，5 新民，6 朝阳，7 西区，8 基础园区）
```

### 运行脚本

```
# 预订
python bath-booking.py
# 查询
python bath-check.py
```

### 已知问题（想增加的特性）
- [x] 不能为多人进行填报
- [ ] 无法根据余量判断并适度调整预约时间
- [ ] 上述问题衍生问题：脚本默认所有时间全部可选，所以直接按链接顺序进行时间识别，实际上当所选性别已全部预约完时，会出错（男性则选择女性）。
