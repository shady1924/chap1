import py2neo
from py2neo import Graph, Node, Relationship
from pandas import DataFrame
from pandas import *

py2neo.authenticate("localhost:7474", "neo4j", "neo4j1")

graph = Graph("http://localhost:7474/db/data/")

def DeleteNode(nodeId ):
    str= "match (n)  where id(n) =" + str(nodeId) +" DETACH DELETE n"
    results=graph.run("""match (a:User)-[:FRIEND*..]-(b:User) return b """)
    
def CreateObjects():
    # 1. For each type of nodes, create one more node of this type. For each type of relationships, 
    # create one more relationship of this type. You can make up the values of properties; 
    testEmployee=Node("Employee", lastName="testEmp",firstName="testEmp",employeeID=1,title="Sales Representative")
    testOrder=Node("Order", orderID="9999",shipName="Test Company Shipping")
    testProd=Node("Product", unitPrice=18,productID="999",productName="TestProd" )
    testCategory=Node("Category", description="Test Soft drinks", categoryName="Test Beverages",categoryID="999")
    testSupplier=Node("Supplier", supplierID="9999", companyName="Exotic Liquids")

    emplyee_order = Relationship(testEmployee,"SOLD",testOrder)
    order_product= Relationship(testOrder,"PRODUCT",testProd)
    product_category= Relationship(testProd,"PART_OF",testCategory)
    supplier_product= Relationship(testSupplier,"SUPPLIES",testProd) 
    
    graph.create(emplyee_order|order_product|product_category|supplier_product)

def answer2():
#     For the category “Grains/Cereals”, find the total count of products, the average product price, the maximum product price,
#     and the minimum product price, of this category. Display these information items. 
    results=graph.run("""
                    MATCH (n:Category{categoryName: "Grains/Cereals"})-[r:PART_OF]-(p:Product)
                    with p.productName as name , p.unitPrice as price 
                    return count(name) as cntproduct, max(price) as maxPrice, min(price) as minPrice, avg(price) as avgPrice      
                    """)
    for result in results:
        print(result)

def answer3():
#     Find out how many orders have been placed to buy each product in the category “Grains/Cereals”. 
#     List the total counts of orders for products in a descending order so that we can know which product in this category
#      is the most popular product

    ## Assumption: Note that we want to check which product sales as highest, so even one order can have a product with more units ordered 
    results=graph.data("""
                    MATCH (n:Category{categoryName: "Grains/Cereals"})-[r:PART_OF]-(p:Product)
                    with p 
                    match (p)-[r:PRODUCT]-(o:Order)
                    return p.productName as productName ,sum(r.quantity) as totalQuantityOrdered,count(o.orderID) as orderCount
                    order by totalQuantityOrdered desc , orderCount desc
                    """)

    print(DataFrame(results)) 

def answer4():
#     4. For the order with an OrderID of 10248, find all other orders that share some common products with this order. 
    results=graph.data("""
                    MATCH (o:Order{orderID:"10248"}) -[r:PRODUCT]-(ProductsInOrder:Product)<-[sameProducts:PRODUCT]-(
                    sameOrder:Order)
                    RETURN o.orderID as originalOrderId, ProductsInOrder.productName as ProductName, sameOrder.orderID as SimilarOrderId
                    """)

      
    for index, rws in DataFrame(results).iterrows():
        print (rws['originalOrderId'] , rws['ProductName'],  rws['SimilarOrderId']  )


def answer5():
# 5. Calculate a similarity index between the product with the productID ‘72’ and the product with the productID ‘11’.  
# The value of the similarity index is the total number of common orders that both of these two products are in. 
# Create a new relationship of “Similarity” between these two products to store this similarity index. 
    
    results=graph.run("""
        MATCH p=(n1:Product {productID :"72"})-[r1:PRODUCT]-(o:Order)-[r2:PRODUCT]-(n2:Product {productID :"11"})
                with n1,n2, count(n2.productID) as Similarity 
                //return n1,n2, Similarity
               create( (n1)- [:SIMILARITY {value:Similarity}] -> (n2))
    """)
    
    print(DataFrame(results)) 
    
def answer6():

# 6. Using the similar approach as in above, find the most “similar” product to the product ‘72’ 
# (but you do not need to create the “Similarity” relationship). Then find out what orders this “similar” product is in 
# but product ‘72’ is not in (so you can image that later we can predict what orders can include product ‘72’ in the near future). 
# You need to complete these tasks in a single query.
     
    result = graph.data("""
        MATCH p=(n1:Product {productID :"72"})-[r1:PRODUCT]-(o:Order)-[r2:PRODUCT]-(n2:Product)
        with n1.productName as productName, n2.productName as matchproductName ,  count( o.orderID) as ordercnt  order by count( o.orderID) desc  limit 1 
        match P=(p:Product{productName: matchproductName})-[r1:PRODUCT]-(o:Order)-[r2:PRODUCT]-(p2:Product)
        where not (p:Product{productID :"72"})-[r1:PRODUCT]-(o:Order)
        return p.productName as topMatchingProduct, r1.quantity as quantity , o.orderID as similarProductOrders, p2.productName as SimilarProductsName
        order by o.orderID
    """)
#     
#     for index, rws in DataFrame(result).iterrows():
#         print (rws['topMatchingProduct'] , rws['quantity'],  rws['similarProductOrders'] , rws['SimilarProductsName']  )
    print(DataFrame(result))      

def answer7():
#     7. Remove the employee Anne Dodsworth (and all its relationships) from the Northwind database. 
    result=graph.run(""" 
        MATCH P=(n:Employee {firstName:"Anne" , lastName:"Dodsworth"})-[r]-() detach delete P    
    """)
    
def main():
    CreateObjects()
    answer2()
    answer3()
    answer4()
    answer5()
    answer6()
    answer7()
main()