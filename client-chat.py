from PyQt5 import QtCore, QtMultimedia
from googletrans import Translator
import googletrans
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QWidget, QInputDialog
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import PyQt5.QtCore
import sys
import socket
from cryptography.fernet import Fernet
import time
import pickle
import io
import json
import re
import os
import io



template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>810</width>
    <height>487</height>
   </rect>
  </property>
  <property name="cursor">
   <cursorShape>ArrowCursor</cursorShape>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="windowOpacity">
   <double>1.000000000000000</double>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QFrame" name="frame">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>781</width>
      <height>431</height>
     </rect>
    </property>
    <property name="autoFillBackground">
     <bool>false</bool>
    </property>
    <property name="styleSheet">
     <string notr="true">QFrame{
	border-radius: 10px;
	background-color: #1B1D23;
}</string>
    </property>
    <property name="frameShape">
     <enum>QFrame::NoFrame</enum>
    </property>
    <property name="frameShadow">
     <enum>QFrame::Raised</enum>
    </property>
    <widget class="QPushButton" name="pushButton_4">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>340</y>
       <width>121</width>
       <height>71</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton {
	font: 12pt &quot;Sitka Small&quot;;
    border: none;
    border-radius: 10px;
	background-color:  #3d3a59;
    color: rgb(250, 250, 250);
}
QPushButton:hover{
	background-color: #4a3c73;
}
QPushButton:pressed{
	background-color: #604d94;
}
</string>
     </property>
     <property name="text">
      <string>Информация</string>
     </property>
    </widget>
    <widget class="QPushButton" name="pushButton_2">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>110</y>
       <width>121</width>
       <height>71</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton {
	font: 12pt &quot;Sitka Small&quot;;
    border: none;
    border-radius: 10px;
	background-color:  #3d3a59;
    color: rgb(250, 250, 250);
}
QPushButton:hover{
	background-color: #4a3c73;
}
QPushButton:pressed{
	background-color: #604d94;
}

</string>
     </property>
     <property name="text">
      <string>Примкнуть</string>
     </property>
    </widget>
    <widget class="QPushButton" name="pushButton_6">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>270</y>
       <width>121</width>
       <height>61</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton {
	font: 12pt &quot;Sitka Small&quot;;
    border: none;
    border-radius: 10px;
	background-color:  #3d3a59;
    color: rgb(250, 250, 250);
}
QPushButton:hover{
	background-color: #4a3c73;
}
QPushButton:pressed{
	background-color: #604d94;
}
</string>
     </property>
     <property name="text">
      <string>Очистить</string>
     </property>
    </widget>
    <widget class="QPushButton" name="pushButton">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>40</y>
       <width>121</width>
       <height>61</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton {
	font: 12pt &quot;Sitka Small&quot;;
    border: none;
    border-radius: 10px;
	background-color:  #3d3a59;
    color: rgb(250, 250, 250);
}
QPushButton:hover{
	background-color: #4a3c73;
}
QPushButton:pressed{
	background-color: #604d94;
}
</string>
     </property>
     <property name="text">
      <string>Настройки</string>
     </property>
    </widget>
    <widget class="QPushButton" name="pushButton_3">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>190</y>
       <width>121</width>
       <height>71</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton {
	font: 12pt &quot;Sitka Small&quot;;
    border: none;
    border-radius: 10px;
	background-color:  #3d3a59;
    color: rgb(250, 250, 250);
}
QPushButton:hover{
	background-color: #4a3c73;
}
QPushButton:pressed{
	background-color: #604d94;
}
</string>
     </property>
     <property name="text">
      <string>Переводчик</string>
     </property>
    </widget>
    <widget class="QLineEdit" name="lineEdit">
     <property name="geometry">
      <rect>
       <x>140</x>
       <y>370</y>
       <width>571</width>
       <height>41</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">QLineEdit{
	border-radius: 15px;
	background-color: #fff;
    font: 12pt &quot;Sitka Small&quot;;
}</string>
     </property>
     <property name="text">
      <string/>
     </property>
    </widget>
    <widget class="QListWidget" name="listWidget">
     <property name="geometry">
      <rect>
       <x>140</x>
       <y>40</y>
       <width>631</width>
       <height>321</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">QFrame{
	border-radius: 15px;
	background-color: #3d3a59;
}
QListWidget {
	font: 12pt &quot;Sitka Small&quot;;
    border: none;
    border-radius: 10px;
	background-color:  #3d3a59;
    color: rgb(250, 250, 250);
}</string>
     </property>
    </widget>
    <widget class="QPushButton" name="pushButton_5">
     <property name="geometry">
      <rect>
       <x>720</x>
       <y>370</y>
       <width>51</width>
       <height>41</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton {
    border: none;
     border-radius: 10px;
    background-color:  #3d3a59;
}
QPushButton:hover{
	background-color: #4a3c73;
}
QPushButton:pressed{
	background-color: #604d94;
}
</string>
     </property>
     <property name="text">
      <string/>
     </property>
    </widget>
    <widget class="QFrame" name="frame_2">
     <property name="geometry">
      <rect>
       <x>0</x>
       <y>0</y>
       <width>781</width>
       <height>31</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">QFrame{
	border-radius: 10px;
	background-color:  #3d3a59;
}</string>
     </property>
     <property name="frameShape">
      <enum>QFrame::StyledPanel</enum>
     </property>
     <property name="frameShadow">
      <enum>QFrame::Raised</enum>
     </property>
     <widget class="QPushButton" name="pushButton_7">
      <property name="geometry">
       <rect>
        <x>744</x>
        <y>0</y>
        <width>31</width>
        <height>23</height>
       </rect>
      </property>
      <property name="styleSheet">
       <string notr="true">QPushButton:hover{
	background-color: #4a3c73;
}
QPushButton{
    border:none
}
QPushButton:pressed{
	background-color: #604d94;
}
</string>
      </property>
      <property name="text">
       <string/>
      </property>
     </widget>
     <widget class="QPushButton" name="pushButton_8">
      <property name="geometry">
       <rect>
        <x>704</x>
        <y>0</y>
        <width>31</width>
        <height>23</height>
       </rect>
      </property>
      <property name="styleSheet">
       <string notr="true">QPushButton {
    border: none;
}
QPushButton:hover{
	background-color: #4a3c73;
}
QPushButton:pressed{
	background-color: #604d94;
}
</string>
      </property>
      <property name="text">
       <string/>
      </property>
     </widget>
    </widget>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>810</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

translatorWindows = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>400</width>
    <height>300</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QFrame" name="frame">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>10</y>
     <width>381</width>
     <height>261</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">QFrame{
	border-radius: 10px;
	background-color: #1B1D23;
}</string>
   </property>
   <property name="frameShape">
    <enum>QFrame::StyledPanel</enum>
   </property>
   <property name="frameShadow">
    <enum>QFrame::Raised</enum>
   </property>
   <widget class="QFrame" name="frame_3">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>381</width>
      <height>31</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QFrame{
	border-radius: 10px;
	background-color:  #3d3a59;
}</string>
    </property>
    <property name="frameShape">
     <enum>QFrame::StyledPanel</enum>
    </property>
    <property name="frameShadow">
     <enum>QFrame::Raised</enum>
    </property>
    <widget class="QPushButton" name="pushButton_7">
     <property name="geometry">
      <rect>
       <x>744</x>
       <y>0</y>
       <width>31</width>
       <height>23</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton:hover{
	background-color: #4a3c73;
}
QPushButton{
    border:none
}
QPushButton:pressed{
	background-color: #604d94;
}
</string>
     </property>
     <property name="text">
      <string/>
     </property>
    </widget>
    <widget class="QPushButton" name="pushButton_8">
     <property name="geometry">
      <rect>
       <x>704</x>
       <y>0</y>
       <width>31</width>
       <height>23</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton {
    border: none;
}
QPushButton:hover{
	background-color: #4a3c73;
}
QPushButton:pressed{
	background-color: #604d94;
}
</string>
     </property>
     <property name="text">
      <string/>
     </property>
    </widget>
    <widget class="QPushButton" name="pushButton_13">
     <property name="geometry">
      <rect>
       <x>340</x>
       <y>0</y>
       <width>31</width>
       <height>23</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton:hover{
	background-color: #4a3c73;
}
QPushButton{
    border:none
}
QPushButton:pressed{
	background-color: #604d94;
}
</string>
     </property>
     <property name="text">
      <string/>
     </property>
    </widget>
    <widget class="QPushButton" name="pushButton_14">
     <property name="geometry">
      <rect>
       <x>310</x>
       <y>0</y>
       <width>31</width>
       <height>23</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton:hover{
	background-color: #4a3c73;
}
QPushButton{
    border:none
}
QPushButton:pressed{
	background-color: #604d94;
}
</string>
     </property>
     <property name="text">
      <string/>
     </property>
    </widget>
   </widget>
   <widget class="QFrame" name="frame_4">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>40</y>
      <width>361</width>
      <height>171</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QFrame{
	border-radius: 10px;
	background-color:  #3d3a59;
}</string>
    </property>
    <property name="frameShape">
     <enum>QFrame::StyledPanel</enum>
    </property>
    <property name="frameShadow">
     <enum>QFrame::Raised</enum>
    </property>
    <widget class="QPushButton" name="pushButton_9">
     <property name="geometry">
      <rect>
       <x>744</x>
       <y>0</y>
       <width>31</width>
       <height>23</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton:hover{
	background-color: #4a3c73;
}
QPushButton{
    border:none
}
QPushButton:pressed{
	background-color: #604d94;
}
</string>
     </property>
     <property name="text">
      <string/>
     </property>
    </widget>
    <widget class="QPushButton" name="pushButton_10">
     <property name="geometry">
      <rect>
       <x>704</x>
       <y>0</y>
       <width>31</width>
       <height>23</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton {
    border: none;
}
QPushButton:hover{
	background-color: #4a3c73;
}
QPushButton:pressed{
	background-color: #604d94;
}
</string>
     </property>
     <property name="text">
      <string/>
     </property>
    </widget>
    <widget class="QLabel" name="label">
     <property name="geometry">
      <rect>
       <x>20</x>
       <y>10</y>
       <width>121</width>
       <height>21</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">QLabel {
	font: 12pt &quot;Sitka Small&quot;;
    border: none;
    border-radius: 10px;
	background-color:  #3d3a59;
    color: rgb(250, 250, 250);
}</string>
     </property>
     <property name="text">
      <string>Перевести с</string>
     </property>
    </widget>
    <widget class="QLineEdit" name="lineEdit">
     <property name="geometry">
      <rect>
       <x>20</x>
       <y>50</y>
       <width>321</width>
       <height>31</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">QLineEdit{
	border-radius: 15px;
	background-color: #fff;
    font: 12pt &quot;Sitka Small&quot;;
}</string>
     </property>
     <property name="text">
      <string/>
     </property>
    </widget>
    <widget class="QLabel" name="label_2">
     <property name="geometry">
      <rect>
       <x>20</x>
       <y>100</y>
       <width>47</width>
       <height>21</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">QLabel {
	font: 12pt &quot;Sitka Small&quot;;
    border: none;
    border-radius: 10px;
	background-color:  #3d3a59;
    color: rgb(250, 250, 250);
}</string>
     </property>
     <property name="text">
      <string>На</string>
     </property>
    </widget>
    <widget class="QLineEdit" name="lineEdit_2">
     <property name="geometry">
      <rect>
       <x>20</x>
       <y>130</y>
       <width>321</width>
       <height>31</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">QLineEdit{
	border-radius: 15px;
	background-color: #fff;
    font: 12pt &quot;Sitka Small&quot;;
}</string>
     </property>
     <property name="text">
      <string/>
     </property>
    </widget>
    <widget class="QComboBox" name="comboBox">
     <property name="geometry">
      <rect>
       <x>140</x>
       <y>10</y>
       <width>191</width>
       <height>21</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">QComboBox{
	border-radius: 15px;
	background-color: #fff;
    font: 12pt &quot;Sitka Small&quot;;
    color rgb(255, 255, 255)
}
QFrame{
     color: rgb(250, 250, 250);
}</string>
     </property>
    </widget>
    <widget class="QComboBox" name="comboBox_2">
     <property name="geometry">
      <rect>
       <x>50</x>
       <y>100</y>
       <width>291</width>
       <height>21</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">QComboBox{
	border-radius: 15px;
	background-color: #fff;
    font: 12pt &quot;Sitka Small&quot;;
    color rgb(255, 255, 255)
}
QFrame{
     color: rgb(250, 250, 250);
}</string>
     </property>
    </widget>
   </widget>
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>220</y>
      <width>361</width>
      <height>23</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton {
	font: 12pt &quot;Sitka Small&quot;;
    border: none;
    border-radius: 10px;
	background-color:  #3d3a59;
    color: rgb(250, 250, 250);
}
QPushButton:hover{
	background-color: #4a3c73;
}
QPushButton:pressed{
	background-color: #604d94;
}

</string>
    </property>
    <property name="text">
     <string>Сделать</string>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

additionalInformation = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>400</width>
    <height>300</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QFrame" name="frame">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>10</y>
     <width>381</width>
     <height>281</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">QFrame{
	border-radius: 10px;
	background-color:  #3d3a59;
    border-style: solid;
    border-color: #231e30;
    width: 100px; 
    height: 100px;  
    border: 4px solid black;
}</string>
   </property>
   <property name="frameShape">
    <enum>QFrame::StyledPanel</enum>
   </property>
   <property name="frameShadow">
    <enum>QFrame::Raised</enum>
   </property>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>80</y>
      <width>201</width>
      <height>16</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QLabel {
	font: 12pt &quot;Sitka Small&quot;;
    border: none;
    border-radius: 10px;
	background-color:  #3d3a59;
    color: rgb(250, 250, 250);
}</string>
    </property>
    <property name="text">
     <string>Создатель: Булат</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>100</y>
      <width>351</width>
      <height>16</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QLabel {
	font: 12pt &quot;Sitka Small&quot;;
    border: none;
    border-radius: 10px;
	background-color:  #3d3a59;
    color: rgb(250, 250, 250);
}</string>
    </property>
    <property name="text">
     <string>Дата начала работы над проектом: </string>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>140</y>
      <width>211</width>
      <height>16</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QLabel {
	font: 12pt &quot;Sitka Small&quot;;
    border: none;
    border-radius: 10px;
	background-color:  #3d3a59;
    color: rgb(250, 250, 250);
}</string>
    </property>
    <property name="text">
     <string>Дата окончания работы над проектом</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>40</y>
      <width>361</width>
      <height>16</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QLabel {
	font: 12pt &quot;Sitka Small&quot;;
    border: none;
    border-radius: 10px;
	background-color:  #3d3a59;
    color: rgb(250, 250, 250);
}</string>
    </property>
    <property name="text">
     <string>Название проекта:</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_5">
    <property name="geometry">
     <rect>
      <x>70</x>
      <y>60</y>
      <width>281</width>
      <height>16</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QLabel {
	font: 12pt &quot;Sitka Small&quot;;
    border: none;
    border-radius: 10px;
	background-color:  #3d3a59;
    color: rgb(250, 250, 250);
}</string>
    </property>
    <property name="text">
     <string> Месссенджер на socket</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_6">
    <property name="geometry">
     <rect>
      <x>80</x>
      <y>120</y>
      <width>111</width>
      <height>21</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QLabel {
	font: 12pt &quot;Sitka Small&quot;;
    border: none;
    border-radius: 10px;
	background-color:  #3d3a59;
    color: rgb(250, 250, 250);
}</string>
    </property>
    <property name="text">
     <string>17.10.23</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_7">
    <property name="geometry">
     <rect>
      <x>80</x>
      <y>160</y>
      <width>111</width>
      <height>20</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QLabel {
	font: 12pt &quot;Sitka Small&quot;;
    border: none;
    border-radius: 10px;
	background-color:  #3d3a59;
    color: rgb(250, 250, 250);
}</string>
    </property>
    <property name="text">
     <string>2.12.23</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_8">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>180</y>
      <width>261</width>
      <height>16</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QLabel {
	font: 12pt &quot;Sitka Small&quot;;
    border: none;
    border-radius: 10px;
	background-color:  #3d3a59;
    color: rgb(250, 250, 250);
}</string>
    </property>
    <property name="text">
     <string>Используемые технологии:</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_9">
    <property name="geometry">
     <rect>
      <x>80</x>
      <y>200</y>
      <width>281</width>
      <height>21</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QLabel {
	font: 12pt &quot;Sitka Small&quot;;
    border: none;
    border-radius: 10px;
	background-color:  #3d3a59;
    color: rgb(250, 250, 250);
}</string>
    </property>
    <property name="text">
     <string>PyQt5, socket, cryptography, json,</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_10">
    <property name="geometry">
     <rect>
      <x>80</x>
      <y>220</y>
      <width>251</width>
      <height>21</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QLabel {
	font: 12pt &quot;Sitka Small&quot;;
    border: none;
    border-radius: 10px;
	background-color:  #3d3a59;
    color: rgb(250, 250, 250);
}</string>
    </property>
    <property name="text">
     <string>pickle, re, io, os, threading, </string>
    </property>
   </widget>
   <widget class="QLabel" name="label_11">
    <property name="geometry">
     <rect>
      <x>80</x>
      <y>240</y>
      <width>201</width>
      <height>20</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QLabel {
	font: 12pt &quot;Sitka Small&quot;;
    border: none;
    border-radius: 10px;
	background-color:  #3d3a59;
    color: rgb(250, 250, 250);
}</string>
    </property>
    <property name="text">
     <string>googletrans.</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_7">
    <property name="geometry">
     <rect>
      <x>340</x>
      <y>10</y>
      <width>31</width>
      <height>23</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton:hover{
	background-color: #4a3c73;
}
QPushButton{
    border:none
}
QPushButton:pressed{
	background-color: #604d94;
}
</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_8">
    <property name="geometry">
     <rect>
      <x>300</x>
      <y>10</y>
      <width>31</width>
      <height>23</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton:hover{
	background-color: #4a3c73;
}
QPushButton{
    border:none
}
QPushButton:pressed{
	background-color: #604d94;
}
</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

template1 = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>400</width>
    <height>300</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QFrame" name="frame">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>9</y>
     <width>381</width>
     <height>281</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">QFrame{
    border-radius: 10px;
	background-color: #1B1D23;
}</string>
   </property>
   <property name="frameShape">
    <enum>QFrame::StyledPanel</enum>
   </property>
   <property name="frameShadow">
    <enum>QFrame::Raised</enum>
   </property>
   <widget class="QFrame" name="frame_2">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>361</width>
      <height>191</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QFrame{
    border-radius: 10px;
	background-color: #3d3a59;
}</string>
    </property>
    <property name="frameShape">
     <enum>QFrame::StyledPanel</enum>
    </property>
    <property name="frameShadow">
     <enum>QFrame::Raised</enum>
    </property>
    <widget class="QLabel" name="label">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>0</y>
       <width>161</width>
       <height>31</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">QLabel{
    font: 22pt &quot;Sitka Small&quot;;
     color: rgb(250, 250, 250);
}</string>
     </property>
     <property name="text">
      <string>Введите:</string>
     </property>
    </widget>
    <widget class="QLineEdit" name="lineEdit">
     <property name="geometry">
      <rect>
       <x>72</x>
       <y>50</y>
       <width>281</width>
       <height>31</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">QLineEdit{
	border-radius: 15px;
	background-color: #fff;
    font: 12pt &quot;Sitka Small&quot;;
}</string>
     </property>
    </widget>
    <widget class="QLineEdit" name="lineEdit_2">
     <property name="geometry">
      <rect>
       <x>72</x>
       <y>100</y>
       <width>281</width>
       <height>31</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">QLineEdit{
	border-radius: 15px;
	background-color: #fff;
    font: 12pt &quot;Sitka Small&quot;;
}</string>
     </property>
    </widget>
    <widget class="QLineEdit" name="lineEdit_3">
     <property name="geometry">
      <rect>
       <x>72</x>
       <y>149</y>
       <width>281</width>
       <height>31</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">QLineEdit{
	border-radius: 15px;
	background-color: #fff;
    font: 12pt &quot;Sitka Small&quot;;
}</string>
     </property>
    </widget>
    <widget class="QLabel" name="label_2">
     <property name="geometry">
      <rect>
       <x>20</x>
       <y>42</y>
       <width>47</width>
       <height>41</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">QLabel{
    font: 12pt &quot;Sitka Small&quot;;
     color: rgb(250, 250, 250);
}</string>
     </property>
     <property name="text">
      <string>Имя</string>
     </property>
    </widget>
    <widget class="QLabel" name="label_3">
     <property name="geometry">
      <rect>
       <x>20</x>
       <y>100</y>
       <width>47</width>
       <height>31</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">QLabel{
    font: 12pt &quot;Sitka Small&quot;;
     color: rgb(250, 250, 250);
}</string>
     </property>
     <property name="text">
      <string>Ip</string>
     </property>
    </widget>
    <widget class="QLabel" name="label_4">
     <property name="geometry">
      <rect>
       <x>16</x>
       <y>149</y>
       <width>51</width>
       <height>31</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">QLabel{
    font: 12pt &quot;Sitka Small&quot;;
     color: rgb(250, 250, 250);
}</string>
     </property>
     <property name="text">
      <string>Port</string>
     </property>
    </widget>
   </widget>
   <widget class="QPushButton" name="pushButtonCancel">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>220</y>
      <width>171</width>
      <height>41</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton {
	font: 12pt &quot;Sitka Small&quot;;
    border: none;
    border-radius: 10px;
	background-color:  #3d3a59;
    color: rgb(250, 250, 250);
}
QPushButton:hover{
	background-color: #4a3c73;
}
QPushButton:pressed{
	background-color: #604d94;
}
</string>
    </property>
    <property name="text">
     <string>Отменить</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButtonConfirm">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>220</y>
      <width>171</width>
      <height>41</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton {
	font: 12pt &quot;Sitka Small&quot;;
    border-radius: 10px;
	background-color:  #3d3a59;
    color: rgb(250, 250, 250);
    border:50px;
    border-color: rgb(250, 250, 250)
}
QPushButton:hover{
	background-color: #4a3c73;
}
QPushButton:pressed{
	background-color: #604d94;
}
</string>
    </property>
    <property name="text">
     <string>Подтвердить</string>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class TranslatorWindows(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(translatorWindows)
        uic.loadUi(f, self)
        self.setWindowTitle("Переводчик")
        self.setWindowModality(2)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)        
        self.center()
        self.listOfLang = list(googletrans.LANGUAGES.values())
        for i in self.listOfLang:
            self.comboBox.addItem(i)
            self.comboBox_2.addItem(i)
            
        icon1 = QtGui.QIcon()
        icon2 = QtGui.QIcon()
        self.pushButton_13.move(345, 5)
        self.pushButton_14.move(315, 5)
        icon1.addPixmap(QtGui.QPixmap(r"button_Icon\x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(r"button_Icon\-.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_13.setIcon(icon1)
        self.pushButton_14.setIcon(icon2)
        self.pushButton_13.clicked.connect(lambda: self.close())
        self.pushButton_14.clicked.connect(lambda: self.showMinimized())
        self.pushButton.clicked.connect(self.translate)

    def get_key(self, d, value):
        for k, v in d.items():
            if v == value:
                return k    
    
    def translate(self):
        trl = self.comboBox.currentText()
        trrl = self.comboBox_2.currentText()
        trt = str(self.lineEdit.text())
        translator = Translator()
        lenguageForTr = googletrans.LANGUAGES.get(self.get_key(googletrans.LANGUAGES, trrl))
        translation = translator.translate(trt, dest=lenguageForTr)
        self.lineEdit_2.setText(translation.text) 
        
    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
            
    def mouseMoveEvent(self, event):
        try:
            delta = QtCore.QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()
        except AttributeError:
            pass
            
    def mousePressEvent(self, event):
            self.oldPos = event.globalPos()        


class AdditionalInformation(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(additionalInformation)
        uic.loadUi(f, self)
        self.setWindowTitle("Информация")
        self.setWindowModality(2)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)        
        self.center()
        icon1 = QtGui.QIcon()
        icon2 = QtGui.QIcon()
        self.pushButton_7.move(345, 5)
        self.pushButton_8.move(315, 5)
        icon1.addPixmap(QtGui.QPixmap(r"button_Icon\x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(r"button_Icon\-.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon1)
        self.pushButton_8.setIcon(icon2)
        self.pushButton_7.clicked.connect(lambda: self.close())
        self.pushButton_8.clicked.connect(lambda: self.showMinimized())        
        
    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
            
    def mouseMoveEvent(self, event):
        try:
            delta = QtCore.QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()
        except AttributeError:
            pass
            
    def mousePressEvent(self, event):
            self.oldPos = event.globalPos()    


class SetWindows(QWidget):
    def __init__(self, parent=None, signal=None):
        self.nickName = None
        self.port = None
        self.ip = None
        self.signal = signal
        super().__init__()
        f = io.StringIO(template1)
        uic.loadUi(f, self)
        self.setWindowTitle("Настройки")
        self.setWindowModality(2)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.center()
        self.pushButtonConfirm.clicked.connect(self.confirm)
        self.pushButtonCancel.clicked.connect(lambda: self.close())
        if os.path.exists(os.path.join("Information", "aboutUser.json")):
            with open(os.path.join("Information", "aboutUser.json")) as f:
                information = json.load(f)
                self.lineEdit.setText(information["nickName"])
                self.lineEdit_2.setText(information["ip"])
                self.lineEdit_3.setText(information["port"])        
    
    def center(self):
            qr = self.frameGeometry()
            cp = QtWidgets.QDesktopWidget().availableGeometry().center()
            qr.moveCenter(cp)
            self.move(qr.topLeft())
    
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()
    
    def mouseMoveEvent(self, event):
        try:
            delta = QtCore.QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()
        except AttributeError:
            pass
        
    def confirm(self):
        self.nickName = self.lineEdit.text()
        self.ip = self.lineEdit_2.text()
        port = self.lineEdit_3.text()
        sampleIp = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
        
        self.lineEdit.setStyleSheet("border-radius: 7px; font: 12pt 'Sitka Small';")
        self.lineEdit_2.setStyleSheet("border-radius: 7px; font: 12pt 'Sitka Small';")
        self.lineEdit_3.setStyleSheet("border-radius: 7px; font: 12pt 'Sitka Small';")        
        
        if 4 <= len(self.nickName) < 15:
            if not re.match(sampleIp, self.ip) is None:
                if port.isdecimal() and int(port) <= 65535:
                    
                    if not os.path.exists(os.path.join("Information", "aboutUser.json")):
                    
                        with open(os.path.join("Information", "aboutUser.json"), "w") as f:
                            information = {"nickName": self.nickName, "ip": self.ip, "port": port}
                            json.dump(information, f, indent=6)
                    else:
                        with open(os.path.join("Information", "aboutUser.json"), "w") as f:
                            information = {"nickName": self.nickName, "ip": self.ip, "port": port}
                            json.dump(information, f, indent=6)
                            
                    self.close()
                    self.signal.emit(['Update configuration'])
                else:
                    self.lineEdit_3.setStyleSheet("border: 2px solid red; border-radius: 7px; font: 12pt 'Sitka Small';")
                    self.lineEdit_3.setText("Некорректный ввод PORT")
            else:
                self.lineEdit_2.setStyleSheet("border: 2px solid red; border-radius: 7px; font: 12pt 'Sitka Small';")
                self.lineEdit_2.setText("Некорректный ввод IP")
        else:
            self.lineEdit.setStyleSheet("border: 2px solid red; border-radius: 7px; font: 12pt 'Sitka Small';")
            self.lineEdit.setText("Слишком длинный либо слишком короткий ник")


class ThreadMonitor(QtCore.QThread):
    getSignal = QtCore.pyqtSignal(list)
    serverSocket = None
    symetricKey = None
    
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        
    def run(self):
        print(f"the server was started {self.serverSocket}")
        while True:
            if self.serverSocket != None:
                message = self.serverSocket.recv(1024)
                decodeMessage = pickle.loads(message)
                if decodeMessage[0] == "200_OK":
                    
                    self.symetricKey = decodeMessage[-1]
                    self.cipher = Fernet(self.symetricKey)
                    self.getSignal.emit(decodeMessage)
                    
                elif decodeMessage[0] == "100_CONTINUE":
                    decryptedMessage = self.cipher.decrypt(decodeMessage[-1]).decode()
                    decryptedload = ["100_CONTINUE", decodeMessage[1], decryptedMessage]
                    self.getSignal.emit(decryptedload)
                    
            time.sleep(2)
                        
    def send_encrypt(self, information):
        if information[0] == "100_CONTINUE":
            encryptMessage = self.cipher.encrypt(information[-1])
            pickLoad = ["100_CONTINUE", information[1], encryptMessage]
            self.serverSocket.send(pickle.dumps(pickLoad))
            
        elif information[0] == "EXIT":
            encryptMessage = self.cipher.encrypt(information[-1])
            pickLoad = ["EXIT", information[1], encryptMessage]
            self.serverSocket.send(pickle.dumps(pickLoad))


class UserInterface(QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.f = io.StringIO(template)
        
        self.initui()
        self.nickName = None
        self.ip = None
        self.port = None
        self.AbilityToConnect = False
        self.connectMonitor = ThreadMonitor()
        self.connectMonitor.getSignal.connect(self.signalHandler)
        
    def initui(self):
        uic.loadUi(self.f, self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) 
        self.center()
        self.pushButton_7.move(745, 5)
        self.pushButton_8.move(709, 5)
        icon = QtGui.QIcon()
        icon1 = QtGui.QIcon()
        icon2 = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("button_Icon\mn1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(r"button_Icon\x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(r"button_Icon\-.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QtCore.QSize(40, 64))
        self.pushButton_7.setIcon(icon1)
        self.pushButton_7.setIconSize(QtCore.QSize(20, 20))          
        self.pushButton_8.setIcon(icon2)
        self.pushButton_8.setIconSize(QtCore.QSize(25, 20))
        self.pushButton.clicked.connect(self.configure)
        self.pushButton_2.clicked.connect(self.join)
        self.pushButton_3.clicked.connect(self.translate)
        #self.pushButton_4.clicked.connect(self.configure)
        self.pushButton_6.clicked.connect(lambda: self.listWidget.clear())
        self.pushButton_5.clicked.connect(self.sendMessage)
        self.pushButton_7.clicked.connect(lambda: self.close())
        self.pushButton_8.clicked.connect(lambda: self.showMinimized())
        self.pushButton_4.clicked.connect(self.getInfo)
        self.setWindowTitle("Чат-мессенджер")
        
    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
            
    def mouseMoveEvent(self, event):
        try:
            delta = QtCore.QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()
        except AttributeError:
            pass
            
    def mousePressEvent(self, event):
            self.oldPos = event.globalPos()
            
    def updateConfigure(self):
        if os.path.exists(os.path.join("Information", "aboutUser.json")):
            with open(os.path.join("Information", "aboutUser.json")) as file:
                data = json.load(file)
                self.nickName = data['nickName']
                self.ip = data['ip']
                self.port = int(data['port'])    
    
    def sendMessage(self):
        
        if self.AbilityToConnect:
            messageText = self.lineEdit.text()
            if len(messageText) > 0:
                pickLoad = ["100_CONTINUE", self.nickName, messageText.encode()]
                print(pickLoad)
                self.connectMonitor.send_encrypt(pickLoad)
                
                item = QtWidgets.QListWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignLeft)
                item.setText(f"{self.nickName} (ВЫ):\n{messageText}")
                self.listWidget.addItem(item)
                self.lineEdit.setText("")
            else:
                message = "Проверьте соединение с сервером"
                QtWidgets.QMessageBox.about(self, "Оповещение", message)            
    
    def signalHandler(self, value:list):
        if value[0] == 'Update configuration':
            self.updateConfigure()
        
        elif value[0] == "200_OK":
            print("signalHandler don't work")
            self.AbilityToConnect = True
            cellMessage = QtWidgets.QListWidgetItem()
            cellMessage.setTextAlignment(QtCore.Qt.AlignHCenter)
            cellMessage.setText(f"Server{value[1]}\n")
            self.listWidget.addItem(cellMessage)
            print(value)            
    
        elif value[0] == "100_CONTINUE":
            print("signalHandler don't work1")
            cellMessage = QtWidgets.QListWidgetItem()
            cellMessage.setTextAlignment(QtCore.Qt.AlignRight)
            cellMessage.setText(f"{value[1]}:\n {value[-1]}")
            self.listWidget.addItem(cellMessage)
            print(value)            
    
    def getInfo(self):
        self.info = AdditionalInformation()
        self.info.show()
    
    def configure(self):
        self.setWn = SetWindows(self, self.connectMonitor.getSignal)
        self.setWn.show()     
    
    def join(self):
        self.updateConfigure()
        if self.nickName != None:
            try:
                self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.client.connect((self.ip, self.port))
                self.connectMonitor.serverSocket = self.client
                self.connectMonitor.start()
            except Exception as error:
                message = "Проверьте соединение с сервером: 'Ошибка с соединением'"
                QtWidgets.QMessageBox.about(self, "Оповещение", message)            
        else:
            message = "Введите имя во фкладке 'Настройки'!"
            QtWidgets.QMessageBox.about(self, "Оповещение", message)
    
    def translate(self):
        self.tr = TranslatorWindows()
        self.tr.show()
    
    def closeEvent(self, value:QtGui.QCloseEvent):
        try:
            payload = ["EXIT", f"{self.nickName} - left the chat".encode()]
            self.connectMonitor.send_encrypt(payload)
            self.hide()
            time.sleep(3)
            self.client.close()
            self.close()
        except Exception as err:
            print(err)
    
    
def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = UserInterface()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())