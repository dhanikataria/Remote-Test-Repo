package atmmanagement;

import java.sql.ResultSet;
import java.sql.SQLException;

import javax.swing.JOptionPane;
import javax.swing.JPanel;

public class Information {
	
	public void infoButtonAction(JPanel panel2) {
		SQLquery sq = new SQLquery();
		Atmmanagement a = new Atmmanagement();
		String user = a.getUserName();
		try {
			ResultSet rs = sq.executeSQLquery("Select * FROM userinfo where Username='" + user + "'");
			while (rs.next()) {
				JOptionPane.showMessageDialog(panel2, "Name = " + rs.getString(2) + "\nFather's Name = " + rs.getString(3) + "\nAddress = "
								+ rs.getString(4) + "\nCash Available = " + rs.getString(5) + " INR");
			}

		} catch (SQLException e) {
			System.out.println("Error while displaying user information");
		}
	}
}
