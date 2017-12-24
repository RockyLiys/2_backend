# -*- coding: utf-8 -*-
CATEGORY = (
    ("0", "基础知识学习"),
    ("1", "素质培养"),
    ("2", "艺术特长"),
    ("3", "运动与体能"),
    ("4", "认知能力"),
    ("5", "操作能力"),
    ("6", "社交能力"),
)

# 基础知识学习
BASE_KNOWLEDGE = [
    ("0", "语文"),
    ("1", "阅读与写作"),
    ("2", "数学"),
    ("3", "珠心算"),
    ("4", "英语"),
    ("5", "外教口语"),
]
# 素质培养
PROFESSIONAL_SKILLS_TRANING = [
    ("6", "编程"),
    ("7", "科学"),
    ("8", "乐高"),
    ("9", "围棋"),
    ("10", "国际象棋"),
    ("11", "中国象棋"),
    ("12", "机器人"),
    ("13", "思维开发"),
    ("14", "演讲口才"),
    ("15", "戏剧表演"),
    ("16", "书法"),
]
# 艺术特长
ART_FEATURES = [
    ("17", "舞蹈"),
    ("18", "钢琴"),
    ("19", "声乐"),
    ("20", "小提琴"),
    ("21", "尤克里里"),
    ("22", "合唱"),
    ("23", "架子鼓"),
    ("24", "黑管"),
    ("25", "萨克斯"),
    ("26", "绘画"),
    ("27", "创意手工"),
    ("28", "陶艺"),
    ("29", "烹饪"),
    ("30", "摄影"),
    ("31", "花艺"),
]
# 运动与体能
EXERCISE_FITNESS = [
    ("32", "篮球"),
    ("33", "足球"),
    ("34", "乒乓球"),
    ("35", "排球"),
    ("36", "跳绳"),
    ("37", "击剑"),
    ("38", "马术"),
    ("39", "跆拳道"),
    ("40", "游泳"),
    ("41", "高尔夫"),
    ("42", "武术"),
]

ALL_SKILLS = BASE_KNOWLEDGE + PROFESSIONAL_SKILLS_TRANING + ART_FEATURES + EXERCISE_FITNESS

# 培养方向
TRAINING_DIRECTION = (
    ("0", "精英", 35, 35, 30, 100),
    ("1", "学霸", 50, 30, 20, 90),
    ("2", "特长", 25, 55, 20, 100),
    ("3", "运动", 20, 50, 30, 100),
    ("4", "交际", 20, 30, 50, 100),
    ("5", "休闲", 20, 20, 20, 60),
    ("6", "平衡", 30, 35, 35, 100),
)
# 性格类型
CHARACTER_TYPE = (
    ("0", "内向型"),
    ("1", "外向型"),
    ("2", "不确定"),
)
# 能力
ABILITY = (
    ("0", "综合分析能力"),
    ("1", "逻辑推理能力"),
    ("2", "抽象思维能力"),
    ("3", "空间想象能力"),
    ("4", "独立思考能力"),
    ("5", "大局观/整体观"),
    ("6", "专注能力"),
    ("7", "计算能力"),
    ("8", "细致观察能力"),
    ("9", "想象能力"),
    ("10", "记忆能力"),
    ("11", "审美能力"),
    ("12", "手眼协调能力"),
    ("13", "色彩搭配能力"),
    ("14", "表演能力"),
    ("15", "解决问题能力"),
    ("16", "形体控制能力"),
    ("17", "身体柔韧能力"),
    ("18", "肢体协调能力"),
    ("19", "创新能力"),
    ("20", "阅读能力"),
    ("21", "书写能力"),
    ("22", "语言表达能力"),
    ("23", "人际交往能力"),
    ("24", "团队协作能力"),
    ("25", "组织能力"),
    ("26", "领导能力"),
    ("27", "抗挫折/坚韧能力"),
)

# mapping
power_map = {
    "计算能力": "jisuan",
    "领导能力": "lingdao",
    "最早适宜年龄": "fit_age",
    "细致观察能力": "xizhiguancha",
    "分类": "基础知识学习",
    "阅读能力": "yuedu",
    "身体柔韧能力": "shentirouren",
    "周时间占用小时": "zhou_min_hours",
    "空间想象能力": "kongjianxiangxiang",
    "独立思考能力": "dulisikao",
    "抗挫折/坚韧能力": "kangya",
    "抽象思维能力": "chouxiangsiwei",
    "解决问题能力": "jiejuewenti",
    "形体控制能力": "xingtikongzhi",
    "手眼协调能力": "shouyanxietiao",
    "组织能力": "zuzhi",
    "记忆能力": "jiyi",
    "周最少花费最少(*100": "zhou_min_speed",
    "团队协作能力": "tuanduixiezuo",
    "名称": "语文",
    "大局观/整体观": "dajv_zhengti",
    "人际交往能力": "renjijiaowang",
    "创新能力": "chuangxin",
    "色彩搭配能力": "secaidapei",
    "肢体协调能力": "zhitixietiao",
    "逻辑推理能力": "luojituili",
    "书写能力": "shuxie",
    "语言表达能力": "yuyanbiaoda",
    "审美能力": "shenmei",
    "表演能力": "biaoyan",
    "专注能力": "zhuanzhi",
    "想象能力": "xiangxiang"
}