import smtplib 
 
text = "You are being watched" 
 
ml = smtplib.SMTP ('smtp.gmail.com',587) 
 
ml.ehlo() 
 
ml.starttls() 
 
ml.login('adedireadedapo21@gmail.com','password') 
 
ml.sendmail('Shaprapra','adedireadedapo19@gmail.com',text) 
  
ml.close()
