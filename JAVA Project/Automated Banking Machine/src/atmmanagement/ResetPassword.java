package atmmanagement;

import java.awt.Color;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.SQLException;
import java.sql.Statement;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JPasswordField;

public class ResetPassword {
	
	
	public void resetPassAction(JPasswordField oldfield,JPasswordField newfield, JPanel resetpanel, JFrame resetframe){
		try {
			Atmmanagement atmMt = new Atmmanagement();
			String user = atmMt.getUserName();
			String pass = atmMt.getPassword();
			java.sql.Connection con = atmMt.getJDBCcon();
			String old = String.valueOf(oldfield.getPassword());

			if (old.equals(pass)) {
				String passchange = "Update logindb set Password='" + String.valueOf(newfield.getPassword())
						+ "' where Username='" + user + "'";
				Statement cst4 = con.createStatement();
				cst4.executeUpdate(passchange);
				JOptionPane.showMessageDialog(resetpanel, "Password was changed successfully");
				resetframe.setVisible(false);

			} else {
				JOptionPane.showMessageDialog(resetpanel, "Incorrect old password");
			}
		}

		catch (SQLException e) {
			System.out.println("Error while resetting password");
		}
	}

	public void resetpassword() {

		JFrame resetframe = new JFrame();
		resetframe.setLayout(null);
		resetframe.setBounds(650, 300, 600, 300);
		resetframe.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);

		JPanel resetpanel = new JPanel();
		resetpanel.setLayout(null);
		resetpanel.setBounds(0, 0, 600, 300);
		resetpanel.setBackground(Color.GRAY);
		resetframe.add(resetpanel);

		JLabel oldpass = new JLabel("Old Password");
		oldpass.setBounds(100, 60, 200, 30);
		oldpass.setFont(new Font("Times New Roman", Font.BOLD, 25));
		oldpass.setForeground(Color.WHITE);
		resetpanel.add(oldpass);

		JPasswordField oldfield = new JPasswordField();
		oldfield.setBounds(300, 60, 250, 30);
		oldfield.setFont(new Font("Times New Roman", Font.BOLD, 20));
		resetpanel.add(oldfield);

		JLabel newpass = new JLabel("New Password");
		newpass.setBounds(100, 110, 200, 30);
		newpass.setFont(new Font("Times New Roman", Font.BOLD, 25));
		newpass.setForeground(Color.WHITE);
		resetpanel.add(newpass);

		JPasswordField newfield = new JPasswordField();
		newfield.setBounds(300, 110, 250, 30);
		newfield.setFont(new Font("Times New Roman", Font.BOLD, 20));
		resetpanel.add(newfield);

		JButton submitbutton = new JButton("Submit");
		submitbutton.setBounds(100, 185, 140, 60);
		resetpanel.add(submitbutton);
		submitbutton.addActionListener(new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent arg0) {
				resetPassAction(oldfield, newfield,resetpanel,resetframe);
			}
		});

		JButton cancelbutton = new JButton("Cancel");
		cancelbutton.setBounds(350, 185, 140, 60);
		resetpanel.add(cancelbutton);
		cancelbutton.addActionListener(new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent arg0) {
				resetframe.setVisible(false);
			}

		});

		resetframe.setVisible(true);
	}













}
