#%%
%sql
CREATE CATALOG IF NOT EXISTS ecommerce;

#%%
%sql
USE catalog ecommerce;
#%%
%sql
CREATE SCHEMA IF NOT EXISTS ecommerce.bronze;
CREATE SCHEMA IF NOT EXISTS ecommerce.silver;
CREATE SCHEMA IF NOT EXISTS ecommerce.gold;
#%%
%sql
SHOW DATABASES FROM ecommerce;
#%%
# %sql
# DROP CATALOG IF EXISTS ecommerce CASCADE;