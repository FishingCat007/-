using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;


namespace 登录窗口
{
    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            海河流域查询.Form4 form = new 海河流域查询.Form4();
            form.Show();
            

        }

        private void button1_Click(object sender, EventArgs e)
        {
            海河流域查询.Form3 form = new 海河流域查询.Form3();
            form.Show();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            海河流域查询.Form5 form = new 海河流域查询.Form5();
            form.Show();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            海河流域查询.Form5 form = new 海河流域查询.Form5();
            form.Show();
        }

        private void Form2_Load(object sender, EventArgs e)
        {

        }
    }
}
