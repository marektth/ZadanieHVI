CREATE TABLE dataset (
    product_ID int AUTO_INCREMENT,
    FOD varchar(50) NOT NULL,
    LOD varchar(50) NOT NULL,
    ROD varchar(50) NOT NULL,
    TA varchar(50) NOT NULL,
    TurningDirection varchar(50) NOT NULL,
    CONSTRAINT PK_product PRIMARY KEY (product_ID)
);