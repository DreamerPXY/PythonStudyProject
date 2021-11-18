from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

#1.拉取数据
iris = load_iris()

#2.数据基本处理
#2.1 数据划分训练集和测试集
train,test,train_target,test_target = train_test_split(iris.data,iris.target,test_size=0.3, random_state=32)
# 3、特征工程：标准化
transfer = StandardScaler()
x_train = transfer.fit_transform(train)
x_test = transfer.transform(test)
# 4、机器学习(模型训练)
estimator = KNeighborsClassifier(n_neighbors=9)
estimator.fit(x_train, train_target)
# 5、模型评估
# 方法1：比对真实值和预测值
y_predict = estimator.predict(x_test)
print("预测结果为:\n", y_predict)
print("比对真实值和预测值：\n", y_predict == test_target)
# 方法2：直接计算准确率
score = estimator.score(x_test, test_target)
print("准确率为：\n", score)