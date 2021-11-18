"""
线性回归
"""
from sklearn.datasets import load_boston
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression,SGDRegressor,Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def linearModel1():
    boston = load_boston()
    x_train,x_test,y_train,y_test = train_test_split(boston.data,boston.target,test_size=0.2,random_state=22)
    stander = StandardScaler()
    x_train = stander.fit_transform(x_train)
    x_test = stander.fit_transform(x_test)
    em = LinearRegression()
    em.fit(x_train,y_train)
    y_predict = em.predict(x_test)
    print(y_predict)

    score = em.score(x_test,y_test)
    print("准确率是:\n",score)

    ret = mean_squared_error(y_test,y_predict)
    print("均方误差是：\n",ret)
def linearModel2():
    boston = load_boston()
    x_train,x_test,y_train,y_test = train_test_split(boston.data,boston.target,test_size=0.2,random_state=22)
    stander = StandardScaler()
    x_train = stander.fit_transform(x_train)
    x_test = stander.fit_transform(x_test)
    em = SGDRegressor(max_iter=2000)
    em.fit(x_train,y_train)
    y_predict = em.predict(x_test)
    print(y_predict)

    score = em.score(x_test,y_test)
    print("准确率是:\n",score)

    ret = mean_squared_error(y_test,y_predict)
    print("均方误差是：\n",ret)

def linearModel3():
    boston = load_boston()
    x_train,x_test,y_train,y_test = train_test_split(boston.data,boston.target,test_size=0.2,random_state=22)
    stander = StandardScaler()
    x_train = stander.fit_transform(x_train)
    x_test = stander.fit_transform(x_test)
    em = Ridge()
    em.fit(x_train,y_train)
    y_predict = em.predict(x_test)
    print(y_predict)

    score = em.score(x_test,y_test)
    print("准确率是:\n",score)

    ret = mean_squared_error(y_test,y_predict)
    print("均方误差是：\n",ret)
if __name__ == '__main__' :
    # linearModel1()
    # linearModel2()
    linearModel3()
