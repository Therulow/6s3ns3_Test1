from package_imports import *

fred = Fred(api_key = os.getenv("API_KEY"))

given_date = "2006-12-01"
df = get_most_recent_series_of_date("BUSLOANS", given_date, fred)
print(df)

pct_chg_commercial_industrial_loans = transform_series(df, 6).dropna()
pct_chg_commercial_industrial_loans.plot()
plt.show()

# print("ADF Test Result: ", adfuller(pct_chg_commercial_industrial_loans))
# plot_acf_pacf(pct_chg_pce['demean_pct_chg'] )
# plot_acf_pacf(pct_chg_pce['demean_pct_chg']**2)
# plt.show()

# #looks like a garch(1, 1) is suitable
# model = arch_model(pct_chg_commercial_industrial_loans, mean = 'AR', lags = 1, vol='Garch', p=1, q=1)
# fit = model.fit()
# # print(fit.summary())

# last_month = pct_chg_commercial_industrial_loans.index[-1]+ pd.offsets.MonthBegin(1)

# #prediction
# pred = fit.forecast(horizon=4-int(last_month.month)%4).mean.iloc[-1].values

# new_dates = pd.date_range(start = last_month , periods = 4-int(last_month.month)%4, freq='MS')
# new_df = pd.Series(pred, index=new_dates)
# pct_chg_pred = pd.concat([pct_chg_commercial_industrial_loans, new_df])

# quarterly_pct_chage = pct_chg_pred.resample('QS').sum()

# def quart_pct_chg_pce(date = "2020-01-01"):
#     return quarterly_pct_chage