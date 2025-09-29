package atmmanagement;

import java.awt.Color;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;

public class WithdrawCash {
	public int avcash;
	

	public void cashwithdraw() {

		JFrame withdrawframe = new JFrame();
		withdrawframe.setLayout(null);
		withdrawframe.setBounds(650, 300, 600, 300);
		withdrawframe.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);

		JPanel withdrawpanel = new JPanel();
		withdrawpanel.setLayout(null);
		withdrawpanel.setBounds(0, 0, 600, 300);
		withdrawpanel.setBackground(Color.GRAY);
		withdrawframe.add(withdrawpanel);

		JLabel cw = new JLabel("Enter the amount");
		cw.setBounds(140, 60, 400, 60);
		cw.setFont(new Font("Times New Roman", Font.BOLD, 40));
		cw.setForeground(Color.WHITE);
		withdrawpanel.add(cw);

		JTextField cwf = new JTextField();
		cwf.setBounds(230, 130, 130, 30);
		cwf.setFont(new Font("Times New Roman", Font.BOLD, 20));
		withdrawpanel.add(cwf);

		JButton subbutton = new JButton("Submit");
		subbutton.setBounds(100, 185, 140, 60);
		withdrawpanel.add(subbutton);
		subbutton.addActionListener(new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent arg0) {
				withdrawAction(cwf, withdrawpanel, withdrawframe);
			}

		});

		JButton canbutton = new JButton("Cancel");
		canbutton.setBounds(350, 185, 140, 60);
		withdrawpanel.add(canbutton);
		canbutton.addActionListener(new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent arg0) {
				// TODO Auto-generated method stub
				withdrawframe.setVisible(false);
			}

		});

		withdrawframe.setVisible(true);

	}

	public void withdrawAction(JTextField cwf, JPanel withdrawpanel, JFrame withdrawframe) {
		Atmmanagement atmmgmt = new Atmmanagement();
		int totalCash = atmmgmt.getTotalCash();
		int enteramt = Integer.parseInt(cwf.getText());
		java.sql.Connection con = atmmgmt.getJDBCcon();
		String user = atmmgmt.getUserName();
		SQLquery sqlqu = new SQLquery();
		try {
			ResultSet rs = sqlqu
					.executeSQLquery("SELECT `Cash_Available` FROM `userinfo` WHERE Username='" + user + "'");
			while (rs.next()) {
				avcash = Integer.parseInt(rs.getString(1));
			}

		} catch (SQLException e) {
			System.out.println("Error while fetching available cash");
		}

		if (enteramt <= totalCash) {
			if (enteramt <= avcash) {
				int accbalance = avcash - enteramt;
				int totleft = totalCash - enteramt;

				try {
					
					String cashwithdrawl = "Update userinfo set Cash_Available='" + accbalance + "' where Username='"
							+ user + "'";
					String cashwithdrawl2 = "Update totalcash set Cash='" + totleft + "'";
					Statement cst6 = con.createStatement();
					cst6.executeUpdate(cashwithdrawl);
					Statement cs7 = con.createStatement();
					cs7.executeUpdate(cashwithdrawl2);
					atmmgmt.setTotalCash();
					JOptionPane.showMessageDialog(withdrawpanel, "Please collect your cash");
					withdrawframe.setVisible(false);

				} catch (SQLException e) {
					e.printStackTrace();
				}

			} else {
				JOptionPane.showMessageDialog(withdrawpanel, "Not enought cash in your account");
			}
		} else {
			JOptionPane.showMessageDialog(withdrawpanel, "Not enough cash in ATM Machine");
		}

	}
}
