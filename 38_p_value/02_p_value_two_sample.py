from scipy import stats
rvs1 = stats.norm.rvs(loc = 5,scale = 10,size = 500)
rvs2 = stats.norm.rvs(loc = 5,scale = 10,size = 500)
print('stats.ttest_ind(rvs1,rvs2):')
print(stats.ttest_ind(rvs1,rvs2))
# Ttest_indResult(statistic = -0.67406312233650278, pvalue = 0.50042727502272966)