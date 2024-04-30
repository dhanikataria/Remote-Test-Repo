package atmmanagement;

import java.awt.Color;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;
import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JPasswordField;
import javax.swing.JTextField;


public class Atmmanagement {

	private static String user, pass;
	private static int totalCash, avcash;
	
	public String getUserName() {
		return user;
	}

	public String getPassword() {
		return pass;
	}
	
	public int getAvCash() {
		return avcash;
	}

	public void setTotalCash() {
		TotalCash tCa = new TotalCash();
		totalCash = tCa.getTotalCash();
	}

	public int getTotalCash() {
		return totalCash;
	}

	public void loginpage() {

		JFrame frame = new JFrame();
		frame.setLayout(null);
		frame.setBounds(650, 300, 600, 300);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		JPanel panel1 = new JPanel();
		panel1.setLayout(null);
		panel1.setBounds(0, 0, 585, 263);
		panel1.setBackground(Color.GRAY);
		panel1.setBorder(BorderFactory.createTitledBorder("Login"));
		frame.add(panel1);

		JLabel ulabel = new JLabel("Username");
		ulabel.setBounds(130, 60, 150, 30);
		ulabel.setFont(new Font("Times New Roman", Font.BOLD, 25));
		ulabel.setForeground(Color.WHITE);
		panel1.add(ulabel);

		JTextField ufield = new JTextField();
		ufield.setBounds(280, 60, 250, 30);
		ufield.setFont(new Font("Times New Roman", Font.BOLD, 20));
		panel1.add(ufield);

		JLabel plabel = new JLabel("Password");
		plabel.setBounds(130, 110, 150, 30);
		plabel.setFont(new Font("Times New Roman", Font.BOLD, 25));
		plabel.setForeground(Color.WHITE);
		panel1.add(plabel);

		JPasswordField pfield = new JPasswordField();
		pfield.setBounds(280, 110, 250, 30);
		pfield.setFont(new Font("Times New Roman", Font.BOLD, 20));
		panel1.add(pfield);

		JTextField tfield = new JTextField();
		tfield.setBounds(280, 110, 250, 30);
		tfield.setVisible(false);
		tfield.setFont(new Font("Times New Roman", Font.BOLD, 20));
		panel1.add(tfield);

		JCheckBox box1 = new JCheckBox("Show Password");
		box1.setBounds(280, 145, 130, 20);
		box1.setFont(new Font("Times New Roman", Font.BOLD, 15));
		panel1.add(box1);
		ShowHidePassword sHPass = new ShowHidePassword();
		box1.addItemListener(new ItemListener() {

			@Override
			public void itemStateChanged(ItemEvent e) {
				if (box1.isSelected()) {
					sHPass.showPassword(pfield, tfield);
				} else {
					sHPass.hidePassword(pfield, tfield);
				}

			}
		});

		JButton okbutton = new JButton("OK");
		okbutton.setBounds(100, 185, 140, 60);
		panel1.add(okbutton);
		Login logIn = new Login();
		okbutton.addActionListener(new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent arg0) {
				user = ufield.getText();
				if(box1.isSelected())
					pass = String.valueOf(tfield.getText());
				else
					pass = String.valueOf(pfield.getPassword());
				
				logIn.loginOkAction(frame, panel1);

			}

		});

		JButton cbutton = new JButton("Cancel");
		cbutton.setBounds(350, 185, 140, 60);
		panel1.add(cbutton);
		cbutton.addActionListener(new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent arg0) {
				System.exit(0);
			}

		});

		frame.setVisible(true);
	}

	public void generalpage() {
		TotalCash tCash = new TotalCash();
		totalCash = tCash.getTotalCash();

		JFrame frame2 = new JFrame();
		frame2.setLayout(null);
		frame2.setBounds(450, 200, 1000, 600);
		frame2.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		JPanel panel2 = new JPanel();
		panel2.setLayout(null);
		panel2.setBounds(0, 0, 1000, 600);
		panel2.setBackground(Color.GRAY);
		frame2.add(panel2);

		JLabel successful = new JLabel("Login Successful!!!");
		successful.setLayout(null);
		successful.setBounds(40, 10, 500, 100);
		successful.setFont(new Font("Times New Roman", Font.BOLD, 45));
		successful.setForeground(Color.WHITE);
		panel2.add(successful);

		JButton infobutton = new JButton("Information");
		infobutton.setBounds(10, 180, 350, 100);
		infobutton.setFont(new Font("Times New Roman", Font.BOLD, 20));
		panel2.add(infobutton);
		Information info = new Information();
		infobutton.addActionListener(new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent arg0) {
				info.infoButtonAction(panel2);
			}
		});

		JButton resetbutton = new JButton("Reset Password");
		resetbutton.setBounds(10, 350, 350, 100);
		resetbutton.setFont(new Font("Times New Roman", Font.BOLD, 20));
		panel2.add(resetbutton);
		ResetPassword resetPass = new ResetPassword();
		resetbutton.addActionListener(new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent arg0) {
				resetPass.resetpassword();
			}
		});

		JButton withdrawbutton = new JButton("Cash Withdrawl");
		withdrawbutton.setBounds(625, 180, 350, 100);
		withdrawbutton.setFont(new Font("Times New Roman", Font.BOLD, 20));
		panel2.add(withdrawbutton);
		WithdrawCash withCash = new WithdrawCash();
		
		withdrawbutton.addActionListener(new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent arg0) {
				withCash.cashwithdraw();
			}

		});

		JButton depositbutton = new JButton("Cash Deposit");
		depositbutton.setBounds(625, 350, 350, 100);
		depositbutton.setFont(new Font("Times New Roman", Font.BOLD, 20));
		panel2.add(depositbutton);
		DepositCash depCash = new DepositCash();
		depositbutton.addActionListener(new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent arg0) {
				depCash.cashdeposit();
			}

		});

		frame2.setVisible(true);
	}
	
	


	public java.sql.Connection getJDBCcon() {
		LoadJDBCdrivers loadDrivers = new LoadJDBCdrivers();
		return loadDrivers.loadDrivers();
	}

	public static void main(String[] args) {
		Atmmanagement loc = new Atmmanagement();
		loc.loginpage();

	}

}
