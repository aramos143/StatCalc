import sys,string
from PyQt5.QtWidgets import QMessageBox,QLabel,QMainWindow,QLineEdit,QApplication,QWidget,QPushButton,QGridLayout
from PyQt5.QtGui import QIcon

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title="Mean, Median, Mode"
        self.x=200
        self.y=200
        self.width=400
        self.height=400
        self.initUI()
            
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.setWindowIcon(QIcon("Pixel_Art_29767.ico"))

        self.createGridLayout()
        self.setLayout(self.layout)
        self.show()
    def createGridLayout(self):
        self.layout=QGridLayout()
        self.layout.setColumnStretch(1,5)
        self.layout.setColumnStretch

        self.textboxlbl=QLabel("Enter List of numbers: ",self)
        self.answerboxlbl=QLabel("Answer Box: ",self)
        self.textbox=QLineEdit(self)
        self.answerbox=QLineEdit(self)
#        self.passwordlbl=QLabel("Password: ",self)
#        self.password=QLineEdit(self)
#        self.password.setEchoMode(QLineEdit.Password)
        self.Mean=QPushButton("Mean",self)
        self.Mean.setToolTip("Compute for Mean")
        self.Median = QPushButton("Median",self)
        self.Mode = QPushButton("Mode",self)
        self.Median.setToolTip("Compute for Median")
        self.Mode.setToolTip("Compute for Mode")
        
        
        self.layout.addWidget(self.textboxlbl, 0,1)
        self.layout.addWidget(self.textbox, 0,2,1,5)
        self.textbox.setPlaceholderText("eg.: 24,26,27,28")
        self.layout.addWidget(self.answerboxlbl, 3,1)
        self.layout.addWidget(self.answerbox, 3,2,1,5)
        self.answerbox.setPlaceholderText("Answer")
#        self.layout.addWidget(self.passwordlbl, 1,1)
#        self.layout.addWidget(self.password, 1,2,1,5)
#        self.layout.addWidget(self.button, 2,2)
        self.layout.addWidget(self.Mean,1,1,1,1)
        self.layout.addWidget(self.Median, 1, 2,1,1)
        self.layout.addWidget(self.Mode, 1, 3,1,1)
        self.Mean.clicked.connect(self.on_mean)
        self.Median.clicked.connect(self.on_median)
        self.Mode.clicked.connect(self.on_mode)
        
        
    def on_mean(self):
        self.checker()
        if self.checker()==False:
            num_list=eval("["+self.textbox.text()+"]")
            mean_ans=sum(num_list)/len(num_list)
            self.answerbox.setText(str(mean_ans))
            
        else:
            self.textbox.clear()
            
            
            
    def on_median(self):
        self.checker()
        if self.checker()==False:
            num_list=eval("["+self.textbox.text()+"]")
            num_list.sort()
            if len(num_list)%2==1:
                median_ans=num_list[(len(num_list)//2)+1]
                print(median_ans)
                self.answerbox.setText(str(median_ans))
            else:
                median_ans=(num_list[int(len(num_list)/2)]+num_list[int((len(num_list)/2)-1)])/2
                self.answerbox.setText(str(median_ans))
        else:
            self.textbox.clear()
    
    
    
    def on_mode(self):
        self.checker()
        if self.checker()==False:
            num_list=eval("["+self.textbox.text()+"]")
            num_list.sort()
            modecheck=(0,0)
            for num in num_list:
                p_mode=num_list.count(num)
                if p_mode > modecheck[0]:
                    modecheck=(p_mode,num)
            self.answerbox.setText(str(modecheck[1]))
                
        else:
            self.textbox.clear()
           
            
    def checker(self):
        if self.textbox.text().isupper() or self.textbox.text().islower():
#            print("Input allowed variables only")
            QMessageBox.warning(self,"","Input allowed variables only",
                                QMessageBox.Ok,QMessageBox.Ok)
            self.answerbox.clear()
            return True
        else:
            return False


if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=App()
    sys.exit(app.exec_())
