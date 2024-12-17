# pip install pandas matplotlib statsmodels openpyxl

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Загрузка данных
file_path = 'example.xlsx'  # Путь к файлу Excel
sheet_name = 'Sheet1'    # Имя листа в Excel
column_name = 'value'    # Название столбца с данными

def analyze_time_series(file_path, sheet_name, column_name, freq):
    # Загружаем данные
    data = pd.read_excel(file_path, sheet_name=sheet_name)
    data['date'] = pd.to_datetime(data['date'])  # Конвертируем время
    data.set_index('date', inplace=True)

    # Декомпозиция временного ряда
    decomposition = seasonal_decompose(data[column_name], model='additive', period=freq)
    trend = decomposition.trend
    seasonal = decomposition.seasonal
    residual = decomposition.resid

    # Отображаем компоненты
    plt.figure(figsize=(12, 8))
    plt.subplot(411)
    plt.plot(data[column_name], label='Original')
    plt.legend(loc='upper left')

    plt.subplot(412)
    plt.plot(trend, label='Trend')
    plt.legend(loc='upper left')

    plt.subplot(413)
    plt.plot(seasonal, label='Seasonality')
    plt.legend(loc='upper left')

    plt.subplot(414)
    plt.plot(residual, label='Residuals')
    plt.legend(loc='upper left')

    plt.tight_layout()
    plt.show()

    print("\n**Основные результаты:**")
    print("- Тренд:\n", trend.dropna().head())
    print("- Сезонность:\n", seasonal.dropna().head())
    print("- Остатки:\n", residual.dropna().head())

# Параметры
freq = 12  # Частота (пример: 12 для ежемесячных данных)

# Запуск функции
analyze_time_series(file_path, sheet_name, column_name, freq)
