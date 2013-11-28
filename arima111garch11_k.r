library(fGarch)
mydata=scan('rate_min.dat')
mydata=ts(mydata)
dev.new()
plot.ts(mydata,xlab='minute',ylab='rate KB/s',main='ARIMA(1,1,1)/Garch(1,1) with 5-step prediction')
fit=garchFit(~arma(1,1,1)+garch(1,1),mydata[1:50])
 
mymu=fit@fitted 
#fitted value,the value for an output variable that has  been predicted by a model fitted to a set of data 
mysd=fit@sigma.t 
#a numeric vector with conditional standard deviation

myseq<-seq(from=51,to=120,by=5)
for(i in 1:length(myseq)){
	fore=predict(fit,n.ahead=5)
	mu=fore$meanForecast
	sd=fore$standardDeviation
	mymu<-c(mymu,mu)
	mysd<-c(mysd,sd)
	fit=garchFit(~arma(1,1,1)+garch(1,1),mydata[1:myseq[i]])
}

upper=mymu+2*mysd
lower=mymu-2*mysd
lines(51:120,mymu[51:120],col='red')
lines(51:120,upper[51:120],col='blue')
lines(51:120,lower[51:120],col='blue')
legend(35,120,c("time series","predicted data","95% Pointwise prediction band"),col=c(1,2,4),lty=1)
