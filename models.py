from django.db import models

class Car(models.Model):
    Car_ID = models.AutoField(primary_key=True)
    SerialNumber = models.CharField(max_length=50, unique=True)
    Make = models.CharField(max_length=50)
    Model = models.CharField(max_length=50)
    Colour = models.CharField(max_length=30)
    Year = models.PositiveIntegerField()
    CarForSale = models.BooleanField(default=True, verbose_name="Car For Sale (Y/N)")

    def __str__(self):
        return f"{self.Make} {self.Model} ({self.Year})"

    #customer
    class Customer(models.Model):
        Customer_ID = models.AutoField(primary_key=True)
        LastName = models.CharField(max_length=50)
        FirstName = models.CharField(max_length=50)
        PhoneNumber = models.CharField(max_length=20)
        Address = models.CharField(max_length=200)
        City = models.CharField(max_length=50)
        StateProvince = models.CharField(max_length=50)
        Country = models.CharField(max_length=50)
        PostalCode = models.CharField(max_length=20)

        def __str__(self):
            return f"{self.FirstName} {self.LastName}"

        #
        # SALESPERSON
        #
        class Salesperson(models.Model):
            Salesperson_ID = models.AutoField(primary_key=True)
            LastName = models.CharField(max_length=50)
            FirstName = models.CharField(max_length=50)

            def __str__(self):
                return f"{self.FirstName} {self.LastName}"

        #
        # SALES INVOICE
        #
        class SalesInvoice(models.Model):
            Invoice_ID = models.AutoField(primary_key=True)
            InvoiceNumber = models.CharField(max_length=30, unique=True)
            Date = models.DateField()
            # Foreign keys to Car, Customer, and Salesperson
            Car_ID = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="sales_invoices")
            Customer_ID = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="sales_invoices")
            Salesperson_ID = models.ForeignKey(Salesperson, on_delete=models.CASCADE, related_name="sales_invoices")

            def __str__(self):
                return f"Invoice {self.InvoiceNumber} ({self.Date})"

        #
        # MECHANIC
        #
        class Mechanic(models.Model):
            Mechanic_ID = models.AutoField(primary_key=True)
            LastName = models.CharField(max_length=50)
            FirstName = models.CharField(max_length=50)

            def __str__(self):
                return f"{self.FirstName} {self.LastName}"

        #
        # SERVICE
        #
        class Service(models.Model):
            Service_ID = models.AutoField(primary_key=True)
            ServiceName = models.CharField(max_length=100)
            HourlyRate = models.DecimalField(max_digits=8, decimal_places=2)

            def __str__(self):
                return self.ServiceName

        #
        # SERVICE TICKET
        #
        class ServiceTicket(models.Model):
            Service_Ticket_ID = models.AutoField(primary_key=True)
            ServiceTicketNumber = models.CharField(max_length=30, unique=True)
            # Foreign keys to Car and Customer
            Car_ID = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="service_tickets")
            Customer_ID = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="service_tickets")
            DateReceived = models.DateField()
            Comments = models.TextField(blank=True, null=True)
            DateReturnedToCustomer = models.DateField(blank=True, null=True)

            def __str__(self):
                return f"Ticket {self.ServiceTicketNumber}"

        #
        # SERVICE MECHANIC
        #
        class ServiceMechanic(models.Model):
            ServiceMechanic_ID = models.AutoField(primary_key=True)
            # Foreign keys to ServiceTicket, Mechanic, and Service
            Service_Ticket_ID = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE,
                                                  related_name="service_mechanics")
            Mechanic_ID = models.ForeignKey(Mechanic, on_delete=models.CASCADE, related_name="service_mechanics")
            Service_ID = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="service_mechanics")
            Hours = models.DecimalField(max_digits=5, decimal_places=2)
            Comment = models.TextField(blank=True, null=True)
            Rate = models.DecimalField(max_digits=8, decimal_places=2)

            def __str__(self):
                return f"Mechanic {self.Mechanic_ID} on Ticket {self.Service_Ticket_ID}"

        #
        # PARTS
        #
        class Parts(models.Model):
            Parts_ID = models.AutoField(primary_key=True)
            PartNumber = models.CharField(max_length=50, unique=True)
            Description = models.TextField(blank=True, null=True)
            PurchasePrice = models.DecimalField(max_digits=8, decimal_places=2)
            RetailPrice = models.DecimalField(max_digits=8, decimal_places=2)

            def __str__(self):
                return f"{self.PartNumber} - {self.Description}"

        #
        # PARTS USED
        #
        class PartsUsed(models.Model):
            Parts_Used_ID = models.AutoField(primary_key=True)
            # Foreign keys to Parts and ServiceTicket
            Part_ID = models.ForeignKey(Parts, on_delete=models.CASCADE, related_name="parts_used")
            Service_Ticket_ID = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE, related_name="parts_used")
            NumberUsed = models.PositiveIntegerField()
            Price = models.DecimalField(max_digits=8, decimal_places=2)

            def __str__(self):
                return f"{self.NumberUsed} x {self.Part_ID.PartNumber} on Ticket {self.Service_Ticket_ID}"