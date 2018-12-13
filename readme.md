# Document Sharing System
Complete v1.0<br/>

# Environment Setup
Install and complete setup Ngrok<br/>
Signup Firebase account and setup Firebase Storage and Firebase Database<br/>

# Firebase Credential Setup
Download database secret key json file from Firebase<<br/>
Put json in all `/Firebase_cred` folder<br/>
Open `Firebase.py` to modifiy json location<br/>

# Run
Run from `/GUI/login.py`<br/>

# Screenshots
#### Real Time Editing<br/>
![Alt text](/images/RealTimeEdit.gif?raw=true)<br/>
#### Sign Up GUI<br/>
![Alt text](/images/Signup.png?raw=true)<br/>
#### Login Up GUI<br/>
![Alt text](/images/login.png?raw=true)
#### Main Window for GU<br/>
![Alt text](/images/GUMainWindow.png?raw=true)
#### Main Window for OU<br/>
![Alt text](/images/OUMainPage.png?raw=true)
#### Main Window for SU<br/>
![Alt text](/images/SUMainWindow.png?raw=true)

# Functionality
#### GU
  1: Double clicks any of the documents in any categories and open up an editor window<br/>
        
  2: Click the `complaint` button in the editor to send complaint to SU<br/>
        
  3: Click the `Suggestion Taboo` button in the editor to send suggestion taboo to SU<br/>
        
  4: Click the `History` button in the editor to view all the history of the current document and double clicks any version to view the change<br/>
                
  5: Click the `sign up` button on the left bottom corner to apply to be OU, need to wait `for` SU to approval. Follow the same step as the Sign Up GUI above<br/>

#### OU
   Similar window to GU and functionalities, but OU has a section for his/her document list<br/>          
  1: Able to search oher OU information based on his/her name<br/>
         
  2: Able to search within own documents by enter a keyword and return a list of the documents contains the keyword<br/>
           
  3: Click the `New Document` button to create a new document and open an editor window<br/>
   > Once enter the name of the document and the context, OU can click `save` button to save the document<br/>
   
   > Or just close the window after finished editing, auto-save feature will save your document<br/>
   
   > If the document is already in the database, `save` button will become `lock` or `unlock` based on the document's current status. User can lock he's own file to prevent unauthorized changes.<br/>
           
  4: Inside of the eiditor window, OU can click the `shared` button to change the type of the document to public, private, and access only through share<br/>
         
  5: In the OU main window, user can view the invitation from other OU, he/she can either accept the inviation or decline the inviation<br/>
           - once the inviation is accepted, he/she can view the documents by clicking `connect` in the `invitation` tab to open the document and perform realtime editing<br/>

#### SU
  SU has all the functionalities from GU and OU, it can maintain the whole system<br/>
  > **For empty database, first create a user with username: `llhc@gmail.com` with password: `csc322` to become a SU**<br/>
  
  1. Under `Taboo Word List` tab, SU can accept suggested taboo words or delete the current effective taboo words<br/>
  
  2. Under `GU Application` tab, SU can see all the GU's applications to either approve or reject their application to become OU<br/>
  
  3. Under `Complaints` tab, SU can have a list of all users' complaints, after complaints is resolve, click `resolve` button to dismiss a complaint<br/>
  
  4. Under `Locked Document` tab, SU can unlock a locked file<br/>
  
  5. `Main` tab is the SU's own document editing page, which is same as OU's main page<br/>


# Team Members:
KaiHang Chen<br>
Haoran He<br>
JinFeng Lin<br>
YanFeng Lin<br>

# Team Name:
LLHC

# Backend:
Python<br>
Socket.io<br>
Firebase<br>
Ngrok<br/>

# Frontend:
PYQT5
