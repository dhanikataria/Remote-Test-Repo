package atmmanagement;

import java.sql.ResultSet;

public class TotalCash {
	
	int tlCash;
	public int getTotalCash() {
		try {
			SQLquery sqlQ = new SQLquery();
			ResultSet rs = sqlQ.executeSQLquery("Select * FROM totalcash");
			while (rs.next()) {
				tlCash = Integer.parseInt(rs.getString(1));
			}
			return tlCash;

		} catch (Exception e) {
			System.out.println("Error while getting Total Cash");
			return 0;
		}
	}
}
