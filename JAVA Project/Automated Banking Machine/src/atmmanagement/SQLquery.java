package atmmanagement;

import java.sql.ResultSet;
import java.sql.Statement;

public class SQLquery {
	
	
	
	public ResultSet executeSQLquery(String query) {
		Atmmanagement atm= new Atmmanagement();;
		try{
			java.sql.Connection con = atm.getJDBCcon();
			Statement cst = con.createStatement();
			ResultSet rs = cst.executeQuery(query);
			
			return rs;
		} catch(Exception e) {
			System.out.println("Error while executing SQL query: "+query);
			return null;
		}
	}
}
