from mysql_functions import mysql_select, mysql_connection_to_server
from psql_functions import psql_insert, psql_connection


def export_mysql_to_pgsql():
	mysql_connection_to_server()
	psql_connection("ANTON")
	data_mysql = mysql_select("ANTON", "carSale")
	for row in data_mysql:
		psql_insert(row)
