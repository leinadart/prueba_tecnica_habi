from abc import ABC
import mysql.connector
import logging

from app.domain.dto.property_dto import PropertyDto
from app.domain.dto.query_data_dto import QueryDataDto
from app.domain.ports.storage_port import StoragePort

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)



class MySqlDBAdapter(StoragePort):


    def __init__(self, host: str, user: str, password: str, database: str, port: str):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port

    def get_data(self, query_data:QueryDataDto) -> list:
        conditionals = ""

        conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            port=self.port
        )

        query = ('''
            SELECT 
                COALESCE(NULLIF(p.address , ''), 'Sin direccion'),
                COALESCE(NULLIF(p.city, ''), 'Sin ciudad'),
                s.name,
                p.price,
                COALESCE(NULLIF(p.description , ''), 'Sin descripcion'),
                MAX(sh.update_date) AS last_update
            FROM habi_db.status_history sh
            LEFT JOIN habi_db.property p 
                ON p.id = sh.property_id
            LEFT JOIN habi_db.status s
                ON sh.status_id = s.id
            WHERE s.name IN ('pre_venta', 'en_venta', 'vendido')
            {conditionals}
            GROUP BY 
                p.id, p.address, p.city, p.description, p.price;
        ''')



        if query_data.year:
            conditionals = f" AND p.`year` = {query_data.year}"
        if query_data.city:
            conditionals = conditionals + f" AND p.city = '{query_data.city}'"
        if query_data.state:
            conditionals = conditionals + f" AND s.name = '{query_data.state}'"

        query = query.format(conditionals=conditionals)

        logger.info(query)

        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()

        rows = [PropertyDto(*item).to_dict() for item in result]
        return rows

