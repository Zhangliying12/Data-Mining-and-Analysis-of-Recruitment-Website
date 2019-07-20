using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.ServiceModel.Web;
using System.Text;
using MySql.Data.MySqlClient;
using System.Threading;
using System.Diagnostics;

namespace WcfService
{
    // 注意: 使用“重构”菜单上的“重命名”命令，可以同时更改代码、svc 和配置文件中的类名“Service1”。
    // 注意: 为了启动 WCF 测试客户端以测试此服务，请在解决方案资源管理器中选择 Service1.svc 或 Service1.svc.cs，然后开始调试。
    public class Service1 : IService1
    {
        //连接字符串
        private string connstr;
        //连接
        MySqlConnection conn;
        public string GetData(int value)
        {
            return string.Format("You entered: {0}", value);
        }

        public CompositeType GetDataUsingDataContract(CompositeType composite)
        {
            if (composite == null)
            {
                throw new ArgumentNullException("composite");
            }
            if (composite.BoolValue)
            {
                composite.StringValue += "Suffix";
            }
            return composite;
        }

        public string transportPath(string suffer, string level, string place, string job, int pay, string welfare, string finance)
        {
            //存储数据
            string sqlInsert = "insert into db_producePlan values('" + suffer + "','" + level + "','" + place + "','" + job + "','" + pay + "','" + welfare + "','" + finance + "')";
            InstanceMysqlConn();
            MySqlCommand cmd = new MySqlCommand(sqlInsert, conn);
            conn.Open();
            try
            {
                cmd.ExecuteNonQuery();
            }
            catch (Exception e)
            {
            }
            conn.Close();

            string Path = "C:/GraduateSchedule/schedule.txt";


            //启动分析程序
            Process proc = Process.Start("C:/Users/79000/Desktop/实训/数据分析/dist/analyse.exe");
            if (proc != null)
            {
                proc.WaitForExit();
            }
            //Thread.Sleep(10000);

            return Path;
        }
        public string login(string username, string password)
        {
            //如果Msg初始化值没有发生变化，说明没有找到该用户
            string Msg = "uninitial";
            //string Pwd = "uninitial";
            string sqlQuery = "SELECT * FROM db_user";
            InstanceMysqlConn();
            MySqlCommand command = new MySqlCommand(sqlQuery, conn);
            conn.Open();
            MySqlDataReader reader = command.ExecuteReader();
            try
            {
                while (reader.Read() == true)
                {
                    if (reader["username"].ToString() == username)
                    {
                        if (reader["password"].ToString() != password)
                            Msg = "PwdFail";
                        else
                            Msg = "Success";
                    }
                }
            }
            catch (Exception ex)
            {

            }
            conn.Close();
            return Msg;
        }

        public string signin(string username, string password)
        {
            string Msg = "uninitial";
            string sqlQuery = "SELECT * FROM db_user";
            string sqlInsert = "insert into db_user(username,password) values('" + username + "','" + password + "')";
            InstanceMysqlConn();
            //判断传递参数
            //判断是否用户名为空
            //验证重名账户
            MySqlCommand command = new MySqlCommand(sqlQuery, conn);
            try
            {
                conn.Open();
            }
            catch(Exception e)
            {
                Console.WriteLine(e.Message);
            }
            MySqlDataReader reader = command.ExecuteReader();
            try
            {
                while (reader.Read() == true)
                {
                    //查找重复用户名
                    if (reader["username"].ToString() == username)
                    {
                        Msg = "UserExist";
                        conn.Close();
                        return Msg;
                    }
                }
            }
            catch (Exception e)
            {
            }
            conn.Close();
            //开始插入账户信息
            conn.Open();
            MySqlCommand cmd = new MySqlCommand(sqlInsert, conn);
            try
            {
                cmd.ExecuteNonQuery();
            }
            catch (Exception e)
            {
                Msg = "SignInFail";
                conn.Close();
                return Msg;
            }
            conn.Close();
            Msg = "Success";
            return Msg;
        }
        //数据库改变时这里配置你的数据库信息
        private void InstanceMysqlConn()
        {
            connstr = "server=localhost; user id=root; password=root; database=job_info;";
            conn = new MySqlConnection(connstr);
        }

    }
}
