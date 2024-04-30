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

public class DepositCash {
	public static int avcash;
	
	
	public void cashDepositAction(JTextField cdf, JPanel depositpanel, JFrame depositframe){ 
		Atmmanagement at = new Atmmanagement();
		String user = at.getUserName();
		int totalCash = at.getTotalCash();
		java.sql.Connection con = at.getJDBCcon();
		
		int enteramt1 = Integer.parseInt(cdf.getText());

		try {
			SQLquery s = new SQLquery();
			ResultSet rs7 = s.executeSQLquery("Select Cash_Available FROM userinfo where Username='" + user + "'");
			while (rs7.next()) {
				avcash = Integer.parseInt(rs7.getString(1));
			}

		} catch (SQLException e) {
			System.out.println("Error while getting available cash");
		}

		int accbalance = avcash + enteramt1;
		int totleft = totalCash + enteramt1;

		try {
			String cashwithdrawl3 = "Update userinfo set Cash_Available='" + accbalance + "' where Username='"
					+ user + "'";
			String cashwithdrawl4 = "Update totalcash set Cash='" + totleft + "'";
			Statement cst8 = con.createStatement();
			cst8.executeUpdate(cashwithdrawl3);
			Statement cs9 = con.createStatement();
			cs9.executeUpdate(cashwithdrawl4);
			at.setTotalCash();
			JOptionPane.showMessageDialog(depositpanel, "Cash was successfully deposited");
			depositframe.setVisible(false);

		} catch (SQLException e) {
			e.printStackTrace();
		}
		
		
	}
	
	
	public void cashdeposit() {
		
		JFrame depositframe = new JFrame();
		depositframe.setLayout(null);
		depositframe.setBounds(650, 300, 600, 300);
		depositframe.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);

		JPanel depositpanel = new JPanel();
		depositpanel.setLayout(null);
		depositpanel.setBounds(0, 0, 600, 300);
		depositpanel.setBackground(Color.GRAY);
		depositframe.add(depositpanel);

		JLabel cd = new JLabel("Insert cash using envelope provided");
		cd.setBounds(140, 60, 400, 60);
		cd.setFont(new Font("Times New Roman", Font.BOLD, 25));
		cd.setForeground(Color.WHITE);
		depositpanel.add(cd);

		JTextField cdf = new JTextField();
		cdf.setBounds(230, 130, 130, 30);
		cdf.setFont(new Font("Times New Roman", Font.BOLD, 20));
		depositpanel.add(cdf);

		JButton subbutton1 = new JButton("Submit");
		subbutton1.setBounds(100, 185, 140, 60);
		depositpanel.add(subbutton1);
		subbutton1.addActionListener(new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent arg0) {
				cashDepositAction(cdf, depositpanel, depositframe);

			}

		});

		JButton canbutton1 = new JButton("Cancel");
		canbutton1.setBounds(350, 185, 140, 60);
		depositpanel.add(canbutton1);
		canbutton1.addActionListener(new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent arg0) {
				// TODO Auto-generated method stub
				depositframe.setVisible(false);
			}

		});

		depositframe.setVisible(true);
	}
}
