////////////////////////////////////////////// 
//服务器端程序               // 
//多用户聊天室              // 
// ChatServer_DB.java         // 
//是Application在单机运行    // 
//姓名：                        // 
//20XX 年XX月XX日        // 
/////////////////////////////////////////////// 
//ChatServer_DB.java   -Xlint:unchecked 
import java.awt.*;    
import java.io.*; 
import java.net.*; 
import java.util.*; 
import java.awt.event.*; 
public class ChatServer_DB extends Thread{ 
    public final static int PORT=8888; 
    ServerSocket ss; 
    java.awt.List user_list;//生成用户列表； 服务器中的那个列表
    Vector users; 
    Vector connections; 
    String username;//当前登录用户 
    String passwd; //当前登录用户密码 
     
    public synchronized void removeUser(String S_user,Connection1 con){ //线程同步 从服服务器中删除
         user_list.remove(S_user); 
         users.remove(S_user); 
         connections.remove(con); 
    } 
    public void out_println(String str){//将跟踪信息显示在 DOS 界面上 
      System.out.println(str); 
    } 
    public ChatServer_DB()//有类创建对象时才调用这方法，老哥
    {//构造函数初始化服务端界面； 
       super("Server");//  -----------------------------------------------------------？
       try
       {  
           ss=new ServerSocket(PORT); 
       }
       catch(IOException e)
       { 
           e.printStackTrace();  
       } 
             Frame f=new Frame("服务器"); 
             user_list=new java.awt.List(); 
             Button warn=new Button("警告"); 
             Button delete=new Button("踢除"); 
                // warn.setBounds(new Rectangle(108,85,60,20));
               // delete.setBounds(new Rectangle(290,85,60,20)); 
             Panel p2=new Panel(); 
             p2.add("West",warn); 
             p2.add("East",delete); 
     warn.addMouseListener(new java.awt.event.MouseAdapter(){ 
    public void mouseClicked(MouseEvent e){ 
      //8、"警告"操作，言论不合法，警告!!,并公布给大家 false,不删除false 
      serverWriter("用户"+user_list.getSelectedItem()+"言论不合法，警告!!!!!",false,null,false); 
    } 
     }); 
     delete.addMouseListener(new java.awt.event.MouseAdapter(){ 
    public void mouseClicked(MouseEvent e){ //监听肯定是在建立好线程的时候，有事件触发才可以调用serverWriter()方法，不用担心还没有传递数据流对象就调用这方法
       String S_user=user_list.getSelectedItem();//选中删除用户   26 
      //7、"踢除"("删除")操作，公布给大家false,并删除!!true，删除者S_user 
         serverWriter("用户"+S_user+"言论不合法，不适合聊天，删除!!",false,S_user,true); 
      //在serverWriter中，通过识别"删除!!"来删除 S_user聊客 
    } 
     }); 
           f.add("South",p2); 
     f.add("Center",user_list); 
     f.setSize(400,200); 
     f.setVisible(true); 
     // f.addWindowListener(new closeWin()); 
            
           f.addWindowListener(new WindowAdapter() 
                     {  public void windowClosing(WindowEvent e) 
                     {   //f.dispose(); 
                         System.exit(0);      } 
                 }); 
 
     users=new Vector(); 
     connections=new Vector(); 
     start(); 
     out_println("服务器运行成功！"); 
    }//public ChatServer_DB() 构造函数相当于在连接服务器页面中设置了三个监听器
    public void run()
    {//用户登录线程启动（主线程启动） 
     try{
         while(true)
        {   
                     out_println("主线程启动！\n"); 
                     Socket s=ss.accept();//侦听并接受到此套接字的连接      每来一个账户，为每一个用户进行发放一个端口，防止发生阻塞
                     out_println("侦听启动！\n"); 
                     Connection1 c=new Connection1(s,this);//this 为 ChatServer_DB()对象 调用connectionl 传递套接字连接对象，使得读取数据时按照指定的端口
                     out_println("主线程c："+c+"\n"); 
                     ServerTaber_DB js=new ServerTaber_DB();//创建数据库操作对象    1
                     out_println("创建数据库操作对象\n"); 
                      username=c.readData(); //方法调用  读出来名字和密码，两个线程都是调用的一个端口
                     passwd=c.readData(); 
                     out_println("主线程启动！"+username+"\n"); 
                     String str2=new String(); 
      //注册：用户名前端系统加"%%%%%"，表示客户端为注册操作 
      if(username.startsWith("%%%%%"))
       { 
          String b=username.substring(5); 
        try
        {//数据库操作，查询此用户密码 
            str2=js.queryTable("select passwd from userlist where name='"+b+"';"); 
            str2 = str2.trim(); 
        }
        catch(Exception e){} 
//如果数据库中没有此用户密码，返回空时则加上"$$$$$$" 
//以username 和passwd注册插入更新数据库; 
          if(str2.equals("$$$$$$"))
          {   
            try
            {// 
                 js.insertRec("insert into userlist (name,passwd) values (?,?);",b,passwd); 
            }
            catch(Exception e){} 
          c.writeData("right");//告知用户注册成功 
          out_println(username+"注册成功！\n"); 
          }else c.writeData("error"); 
      }//if 
//连接：用户名前端系统没有加"%%%%%"，表示客户端为连接操作 
        if(!username.startsWith("%%%%%"))
        {//无重名  break跳出循环，可以连接 
          while(true)//*********************************************************//用户名称和密码可以多次输入**************************对密码用户名的处理
         {// 
          try
          {// 
            str2=js.queryTable("select passwd from userlist where name='"+username+"';"); 
            str2 = str2.trim(); 
          }
          catch(Exception e){} 
          if(passwd.equals(""+str2)&&(!users.contains(username))) 
               break;//跳出循环，可以连接 
          if(!passwd.equals(""+str2)) 
          c.writeData("error1");//密码错误或数据库没有连上 
          if(users.contains(username)) 
          c.writeData("error2");//有重名或以登录 
           
          username=c.readData();//循环等候接收新的用户名 
          passwd=c.readData(); 
         }//while(true) **********************************************************************************
                c.writeData("right");//可以连接 
                c.username=username; 
                c.start(); //连接成功 启动那个线程********登录后聊天线程   *********开始对信息登陆后发送信息的处理
          synchronized(users)
          {//同步实现加载用户 
           users.addElement(username); 
           connections.addElement(c); 
           user_list.add(username); 
          } ///----------------------老师问的用户怎么加载到服务器对话框的答案
        //1、"加入"告知大家（你对大家），包括自己 
          //登录成功，信息发布给大家，添加到用户列表中 
          //登录用户 username告知大家（公聊、不踢除） 
          serverWriter("用户"+username+"加入",false,null,false);//公聊false 
          out_println("用户："+username+"登录成功！null"); 
                 
        //2、"加入"，大家对你，将已有用户名加入到你的列表框中 
          //在新用户登录后，列表框中加入已有用户名，不包括自己 
          Enumeration em=users.elements();//已有用户向量 
          while(em.hasMoreElements()){ 
            String str=(String)em.nextElement(); 
            if (!str.equals(username)){//不包括自己，大家对你私聊 
               serverWriter("用户"+str+"加入",true,username,false);//私聊 true 
            }  
          } 
          }//if 
       }//while(true) 
    }catch(IOException e){  e.printStackTrace();} 
   }//run 
  public synchronized void serverWriter(String str,boolean w,String S_user,boolean b_delete){   
    Enumeration em=connections.elements();//连接线程用户向量枚举 
    Connection1 c_delet=null; 
    while(em.hasMoreElements()){//枚举循环 
      Connection1 c=(Connection1)em.nextElement(); 
      if(w)
      {            //私聊true 
        if(c.username.equals(S_user))//匹配私聊对象S_user，以连接用户线程 c.username 
          c.writeData(str+"\n"); 
          
      }
      else
      {           //公聊false 
        //if (!S_user.equals(c.username)||str.indexOf("加入")!=-1 ){//不包括自己 
           c.writeData(str+"\n");   //不匹配聊天对象S_user=null 
           out_println("c："+c+";S_c:"+c.username+";S_user:"+S_user+";str:"+str+"\n"); 
        //} 
       }//if 
      if(b_delete)
      {//"删除"操作：匹配删除对象 S_user。不包括"退出" 
        if(c.username.equals(S_user))
        {//匹配删除对象S_user 
          c_delet=(Connection1)c; 
        } 
      } 
    }//while 
    if(b_delete && c_delet.username.equals(S_user)){//删除匹配对象S_user 
      removeUser(S_user,c_delet);//在服务器中删除   29 
      try{ 
        c_delet.dis.close();//c_delet.close();不能用，c_delet没有传过去 
        c_delet.dos.close(); 
        c_delet.s.close(); //删除这个对象的通讯中的数据流信息
      }catch(IOException e){  e.printStackTrace();} 
       out_println("删除！"+S_user+";c_delet:"+c_delet+"\n"); 
    } 
  }// serverWriter() 
  public static void main(String[] args)//*************************************************Main
  {   
      new ChatServer_DB(); 
  } 
}//ChatServer_DB 

class Connection1 extends Thread{ 
    ChatServer_DB cs; 
    Socket s; 
    DataInputStream dis; 
    DataOutputStream dos; 
    public String username; 
     String talker=null; 
    boolean whisper; 
 
    public Connection1(Socket s,ChatServer_DB cs){ 
      this.cs=cs; 
      this.s=s; 
    try{dis=new DataInputStream(s.getInputStream()); 
        dos=new DataOutputStream(s.getOutputStream()); 
         }catch(IOException e){  e.printStackTrace();} 
    cs.out_println("输入输出流启动！\n"); 
   }//Connection1() 
 
    public void run(){//登录后聊天线程 
      String temp; 
    try{ 
      while(true)
      { 
           temp=readData();//返回聊天内容，同时确定username、whisper,talker 
             if (temp.indexOf("退出")!=-1){      
        //3、或 4、"退出"操作，接收退出处理(公聊和私聊) 
        cs.serverWriter(temp,whisper,talker,false);//"["+username+"]"+ 
        cs.out_println("聊天线程退出："+username+";"+temp+"\n"); 
        close();//"退出"在此服务器中删除 
 
      }else{                              
        //5、或 6、"聊天"操作,非退出   30 
        cs.serverWriter("["+username+"]"+temp,whisper,talker,false); 
           cs.out_println("聊天线程启动："+username+"\n"); 
      }    
       }//while 
         }catch(IOException e2){} 
    finally{  //close(); 
    } 
     }//run() 
 
    public void close(){   
        cs.removeUser(username,this); 
     try{    dis.close(); 
             dos.close(); 
             s.close(); 
         }catch(IOException e){} 
     //cs.serverWriter("用户"+username+"退出",false,null,true);//公聊，告知所有聊客，退出 
    }//close() 
    
  //返回聊天内容 
    public String readData() throws IOException{ 
       String temp=dis.readUTF(); 
       if(temp.charAt(0)=='#')
       { //私聊，确定username、whisper,talker 
      whisper=true;                  //私聊 
      int kk=temp.indexOf('#',1); 
      talker=temp.substring(1,kk);   //私聊对象 
      return new String(temp.substring(kk+1));//聊天内容 
       } 
       whisper=false;//公聊 
       talker=null; 
     return new String(temp.substring(1));//聊天内容 
     }// readData() 
 
  public void writeData(String str) { 
      try{dos.writeUTF(str); 
        dos.flush(); 
      }catch(IOException e){  e.printStackTrace();} 
     }//writeData() 
}//Connection1

/*
 * 主线程中是做了一些对话框的监听设置，对登陆注册功能做处理（加载到服务器中的对话框和登录用户的对话框)对聊天的公聊和私聊做出处理，在服务器中删除用户信息
 * 
 */

