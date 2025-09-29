package atmmanagement;

import java.sql.ResultSet;
import java.sql.SQLException;

import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;


public class Login {
	
public void loginOkAction(JFrame frame, JPanel panel1) {
		Atmmanagement atmMgmt = new Atmmanagement();
		SQLquery sqlQue = new SQLquery();
		String user = atmMgmt.getUserName();
		String pass = atmMgmt.getPassword();
		
		try {
			if (user != null && pass != null) {
				String query = "Select Username,Password from logindb Where Username='" + user + "' and Password='" + pass + "'";
				ResultSet rs = sqlQue.executeSQLquery(query);
//				a' or 1=1 -- 
				
//				String   a = "Select Username,Password from logindb Where Username='a' or 1=1"; // " + user + "' and Password='" + pass + "'";
				
//				ResultSet rs = sqlQue.executeSQLquery("Select Username,Password from logindb Where Username='" + user + "' and Password='" + pass + "'");
				int count = 0;
				while (rs.next()) {
					count++;
				}
				if (count != 0) {
					atmMgmt.generalpage();
					frame.setVisible(false);

				} else
					JOptionPane.showMessageDialog(panel1, "Username and Password didn't match");
			}
		}
		catch (SQLException e) {
			System.out.println("Error while executing Username, Password Query");
		}
	}
}
