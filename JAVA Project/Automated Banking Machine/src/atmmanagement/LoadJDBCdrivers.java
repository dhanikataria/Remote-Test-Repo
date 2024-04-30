package atmmanagement;

import java.sql.DriverManager;

public class LoadJDBCdrivers {
	
	public java.sql.Connection loadDrivers() {
		try {
			java.sql.Connection con;
			Class.forName("com.mysql.jdbc.Driver");
			con = DriverManager.getConnection("jdbc:mysql://localhost:3306/atm", "root", "");
			return con;
		} catch (Exception e) {
			System.out.println("Error while loading drivers");
			return null;
		}
	}
}
