def conversion(y_train,stk_data):
    import pandas as pd
    Actual_y_train=pd.DataFrame(index=range(len(y_train)),columns=stk_data.columns)
    for i in range(len(y_train)):
        Actual_y_train.iloc[i]=y_train[i]
    return Actual_y_train

def graph(Actual,predicted,Actlabel,predlabel,title,Xlabel,ylabel):
    from matplotlib import pyplot as plt
    plt.figure(figsize=(10,5))
    plt.plot(Actual, color = 'blue', label=Actlabel)
    plt.plot(predicted, color = 'green', label =predlabel)
    plt.title(title)
    plt.xlabel(Xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()
    
def rmsemape(y_Test,predicted_stock_price_test_ori):
    from sklearn.metrics import mean_squared_error
    print("RMSE-Testset:",mean_squared_error(y_Test,predicted_stock_price_test_ori,squared=False))
    #print("RMSE-Trainset:",mean_squared_error(y_Train,predicted_stock_price_train_ori,squared=False))
    from sklearn.metrics import mean_absolute_percentage_error
    print("maPe-Testset:",mean_absolute_percentage_error(y_Test,predicted_stock_price_test_ori))
    #print("mape-Trainset:",mean_absolute_percentage_error(y_Train,predicted_stock_price_train_ori))


def conversionSingle(y_train,stk_data):
    import pandas as pd
    Actual_y_train=pd.DataFrame(index=range(len(y_train)),columns=stk_data)
    for i in range(len(y_train)):
        Actual_y_train.iloc[i]=y_train[i]
    return Actual_y_train
















    