import sys
from PyQt5 import QtCore, QtGui, QtWidgets

        
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1200,800)
        Form.setMinimumWidth(1200)
        Form.setMinimumHeight(800)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Oxygen-Icons.org-Oxygen-Categories-applications-internet.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color: rgb(94, 94, 94);")
        Form.adjustSize() # Adicionado para ajustar o tamanho do widget automaticamente

        # Vertical layout for the main window
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)

        # Frame for the top section
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)

        # Horizontal layout for the top section
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        #self.horizontalLayout.setSpacing(5)

        # Labels and line edits
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setStyleSheet("font: 10pt \"Arial\";")
        self.label.setObjectName("label")
        self.label.setText("Link:")
        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_nome_jogo = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_nome_jogo.setObjectName("lineEdit_nome_jogo")
        self.lineEdit_nome_jogo.setMinimumWidth(80)
        self.lineEdit_nome_jogo.setMaximumHeight(90)
        self.horizontalLayout.addWidget(self.lineEdit_nome_jogo)

       

       

        # Push buttons
        self.pushButton_atualizar = QtWidgets.QPushButton(self.frame)
        self.pushButton_atualizar.setStyleSheet("font: 9pt \"Arial\";")
        self.pushButton_atualizar.setObjectName("pushButton_atualizar")
        self.pushButton_atualizar.setText("Atualizar")
        #self.pushButton_atualizar.clicked.connect(self.loja)
        
        self.horizontalLayout.addWidget(self.pushButton_atualizar)

        self.pushButton_limpar = QtWidgets.QPushButton(self.frame)
        self.pushButton_limpar.setStyleSheet("font: 9pt \"Arial\";")
        self.pushButton_limpar.setObjectName("pushButton_limpar")
        self.pushButton_limpar.setText("Limpar")
        #self.pushButton_limpar.clicked.connect(self.clear_lineedit)
        self.horizontalLayout.addWidget(self.pushButton_limpar)

        self.pushButton_limpar_tabela = QtWidgets.QPushButton(self.frame)
        self.pushButton_limpar_tabela.setStyleSheet("font: 9pt \"Arial\";")
        self.pushButton_limpar_tabela.setObjectName("pushButton_limpar_tabela")
        self.pushButton_limpar_tabela.setText("Limpar Tabela")
        #self.pushButton_limpar_tabela.clicked.connect(self.limpar_tabela)
        self.horizontalLayout.addWidget(self.pushButton_limpar_tabela)

        

        self.verticalLayout.addWidget(self.frame)
        #vertical Leyout
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout.addWidget(self.frame_2)
                # Table widget
        self.tableWidget = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget.setStyleSheet("font: 10pt \"Arial\";")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        #
        
        header = self.tableWidget.horizontalHeader()

        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(7, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Interactive)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Interactive)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Interactive)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Interactive)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Interactive)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.Interactive)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.Interactive)
        header.setSectionResizeMode(7, QtWidgets.QHeaderView.Interactive)
                
        header.setStretchLastSection(True)
        header.setDefaultSectionSize(self.tableWidget.width()//3)
        header.resizeSection(1, int(self.tableWidget.width()* 3.5))
        header.resizeSection(7, int(self.tableWidget.width() ))
        #self.tableWidget.cellClicked.connect(self.on_cell_clicked)
        
        # Create a vertical layout and add the table widget to it
        vLayout = QtWidgets.QVBoxLayout(self.frame_2)
        vLayout.addWidget(self.tableWidget)

        # Set the layout for the frame
        self.frame_2.setLayout(vLayout)

        # Set the size policy for the frame to be expanding
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.frame_2.setSizePolicy(sizePolicy)
        
        #nomes
        self.retranslateUi(Form)
        #nome,tipo,preco,promo,percent_,link,data,loja
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Banco Games"))
        self.label.setText(_translate("Form", "Nome Jogo:"))
        self.pushButton_atualizar.setText(_translate("Form", "Buscar"))
        self.pushButton_limpar.setText(_translate("Form", "Limpar"))
        self.pushButton_limpar_tabela.setText(_translate("Form", "Limpar Tabela"))
        
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Loja"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Jogo"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Tipo"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Promo"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "% Desconto"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Preço"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Data"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Link"))
if __name__ == "__main__":
    import sys
    rowlist=[]
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())