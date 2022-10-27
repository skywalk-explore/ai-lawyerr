from datetime import date

urlDictionary = {
    'Private Housing - Rent Advice': 'privateHousingRentAdvice',
    'Private Housing - Section 21 Eviction Advice': 'section21EvictionAdvice',
    'Private Housing - Section 8 Eviction' : 'section8EvictionAdvice'
}

privateHousingRentAdviceDict = {
    'twelveMonthRule' : 'You have advised us your landlord increased your rent less than 12 months ago. This is not the correct procedure. Landlords are permitted to increase rent once every 12 months against the same tenant on a Rolling Tenancy. We CAN challenge the rent increase on this ground.',
    'asTenancy': 'You have advised us that your have an Assured Shorthold Tenancy (also known as Fixed Term Tenancy). For Assured Shorthold Tenancies the rent is fixed for the period of the tenancy and can only be increased by the amount agreed in the contract. This type of tenancy agreement the rent is usually fixed for the first year and some type of clause is included noting rent increase in subsequent year if more than 1. Any rent increase will have to adhere to that clause. If no such clause is included, during the fixed term, any rent increase is likely unlawful -- unless agreed by the tenant.',
    'form4GivenOrNot' : 'A rent increase is only valid if all relevant procedure is followed. You have advised us your landlord has not used form 4 to propose the rent increase. This is not the correct procedure. If you are on a Periodic Tenancy (also known as Rolling Tenancy) form 4 must be used to propose a rent increase otherwise any proposed increased is invalid. If you were on an assured shorthold tenancy (also known as Fixed Term Tenancy) that continued after the fixed term finished, serving a form 4 to impose rent increase also become a requirement. Texting, sending emails without the relevant form is not a valid notice.',
    'noticePeriodForIncreaseGiven' : 'You have advised us that your landlord did not give you notice period until the increased rent amount takes effect. This is the incorrect procedure. If your tenancy period is for 1 year, the notice required before rent increase takes effect is six months. If the tenancy period is less than one year, the notice required before the rent increase takes effect is one of the tenancy period. If the tenancy is less than one month or less,  the notice required before rent increase takes effect is one month.',
    'depositAmountAndAdvice' : 'Rent Negotiation Tactic Deposits : ',
    'hmoStatusAndLicenceAdvice' : 'Rent Negotiation Tactic HMO : You have advised us that the property is a HMO but does not have a HMO licence. This a breach of HMO licensing policy. Breach of this policy can result in a rent repayment order against the landlord and they may be asked to repay up to 12 months rent (application for RRO needs to be made within 12 months of breach). If you are unhappy with a landlords rent increase, you can use the HMO breach to negotiate a reasonable increase or even lower the rent.',
    'additionalInfo' : 'Any additional inform provided in the text box will only be addressed by email if you are a paid subscriber to Renting Guide blog. We use the email you have provide to check subscription status.',
}
class PrivateHousingRentAdvice:
    def __init__(self, formData:dict):
        # variable to be passed to jinja2 Template when rendering advice.
        self.title = "Advice on How to Challenge or Negotiate A Rent Amount For Tenants In Private Housing"
        # the dictionary containing the inputs selected by user and passed to backed by request.form.to_dict()
        self.formData = formData
        # data containing advice on socialHousingRent. this will limit import to main py.file
        self.adviceDict = privateHousingRentAdviceDict
        # an empty list containing advice appended using the class methods
        self.advice = []

    def dataBase(self):
        # retaining some core data to see use cases. will be common to all classes.
        with open('../database.txt', 'a') as d:
            # variable documenting time at instance call
            time = date.today()
            # variable document name passed to html form
            name = self.formData['User Name'].title()
            # variable documenting the email passed to html form
            email = self.formData['Email'].title()
            # variable documenting post code passed to html form
            postCode = self.formData['Post Code'].upper()
            # variable documenting HTML form additional data field.
            additionalInfo = self.formData['Additional Info'].title()
            d.write(f"\n{time} :: {name} :: {email} :: {postCode} :: Rent Increase Advice Requested :: {additionalInfo}")

    def asTenancy(self):
        # checks the tenancy Type and offers advice to tenants on an Assured Shorthold Tenancy
        if self.formData['Tenancy Type'] == "Assured Shorthold Tenancy":
            self.advice.append(self.adviceDict["asTenancy"])

    def startedOnAssuredTenancy(self):
        # what to do if you started on an assured shorthold tenancy but stayed on.
        # statutory periodic tenancy (not agreed and a new contract) or contractual periodic tenancy (agreed and not new)
        pass

    def twelveMonthRule(self):
        # checks the tenancy Type and offers advice to tenants on Rolling Tenancy
        if self.formData['Tenancy Type'] == "Rolling Tenancy":
            if self.formData['Las Rent Increase Was'] == 'Less Than 12 Moths Ago':
                self.advice.append(self.adviceDict["twelveMonthRule"])

    def form4GivenOrNot(self):
        # checks whether a valid rent increase notice was served
        if self.formData['Tenancy Type'] == "Rolling Tenancy":
            if self.formData['Notice Served By'] != "Using FORM 4 Rent Increase Notice":
                self.advice.append(self.adviceDict["form4GivenOrNot"])

    def noticePeriodForIncreaseGiven(self):
        # checks whether the proposed rent increase will be increased after the required statutory notice period
        if self.formData['Rent Increase Notice Period Given'] == 'No':
            self.advice.append(self.adviceDict["noticePeriodForIncreaseGiven"])

    def depositAmountAndAdvice(self):
        if self.formData['Deposit Amount'] != "None":
            if self.formData['Deposit Protection Notification Given'] == "No":
                self.advice.append(self.adviceDict["depositAmountAndAdvice"])
            elif self.formData['Deposit Protection Scheme Used'] == "No":
                self.advice.append(self.adviceDict["depositAmountAndAdvice"])

    def hmoStatusAndLicenceAdvice(self):
        if self.formData['Property A HMO'] == 'Yes':
            if self.formData['HMO Licence Status'] == "No":
                self.advice.append(self.adviceDict["hmoStatusAndLicenceAdvice"])

    def additionalInfo(self):
        # checks if the user noted anything the optional form field
        if self.formData['Additional Info']:
            # returns a standard message of we'll get back to you etc.
            self.advice.append(self.adviceDict['additionalInfo'])

    # def blankForm(self):
    #     self.advice.append(self.adviceDict['blankForm'])

    def callMethods(self):
        self.dataBase()
        self.asTenancy()
        self.twelveMonthRule()
        self.form4GivenOrNot()
        self.noticePeriodForIncreaseGiven()
        self.depositAmountAndAdvice()
        self.hmoStatusAndLicenceAdvice()
        self.additionalInfo()

section21EvictionAdviceDict = {
    'additionalInfo' : 'Any additional info provided will be responded to if you are a paid member of the Renters Guide blog or have donated through PayPal or Bitcoin. We will confirm the donation/subscription using your email address. If you are not a member, no contact will be made.',
    'form6aUsed' : 'You have advised us that your landlord has not served you with a Form 6A eviction notice. Section 21 Eviction notices are only valid if they are served using Form 6A or a document containing information that is required in form 6A. Otherwise, the notice is invalid and it can be ignored. If the landlord makes an application to the courts to enforce the eviction, you will have a chance to respond and at that point, you can advise the court about the 6A form and note the landlord has never served a valid eviction notice.',
    'depositRequirementsA' : "Section 21 notices are only valid if the correct procedure was followed in handling the tenant's deposit. You have advised that paid a deposit to your landlord. You have also advised us that the landlord did not place your deposit into a Deposit Protection Scheme. This is not the correct procedure. Deposits have to be placed into an authorised scheme. A landlord who fails to do so cannot serve a valid Section 21 eviction notice. If the landlord makes an application to the courts to enforce the eviction, you will have a chance to respond and at that point, you can advise the court that the Landlord did protect the deposit and therefore cannot serve a valid Section 21 eviction notice.",
    'depositRequirementsB' : "Section 21 notices are only valid if the correct procedure was followed following the placement of the deposit into a Deposit Protection Scheme. You have advised us that paid a deposit to your landlord. You have also advised us that the Landlord did not notify you of whether the deposit was placed into a protection scheme and provided you with the relevant connected information. This is not the correct procedure. If the landlord makes an application to the courts to enforce the eviction, you can advise the court of this failure and note that the eviction notice, as a result, is invalid.",
    'overChargedDeposit' : "You have advised us that the Landlord has charged a deposit which amounts to more than 5 weeks' rent. A deposit higher than 5 weeks’ rent (or 6 weeks if your yearly rent is £50 000 or more) qualifies as a prohibited payment. The section 21 eviction notice is invalid until the overcharged amount is returned. You are protected by this policy if your tenancy started or was renewed after June 1, 2020.",
    'gasSafetyCertificate' : "You have advised us that the landlord has not given a Gas Safety Certificate. For a property with Gas Appliances and/or a gas line, failure to provide this certificate renders any subsequent Section 21 eviction notice that is served become invalid. For the eviction notice to be valid, the Gas Safety Certificate has to be issued before the eviction notice. If the landlord makes an application to the courts to enforce the eviction, you can advise the court of this point.",
    'proscribedInformation' : "You have advised us that the landlord has not provided you with certain items noted on the Proscribed Information list. Any Landlord who fails to provide this information cannot serve a valid notice. If the landlord makes an application to the courts to enforce the eviction, you can advise the court that the Landlord did not provide the proscribed information (and note the specific information that was not given) and therefore a valid Section 21 eviction notice was never served",
    'evictionNoticePeriod' : "You have advised us, in the section 21 eviction notice served, your landlord has not given you a 2 months notice to leave the property. A Section 21 notice must give tenants at least 2 months’ notice to leave the property. If this prescription is not followed, the landlord has not served a valid notice. Beyond this minimum of 2 months' notice, there may be a need for additional notice. If you pay rent every 3 months, or once at a longer period, the Landlord must give notice equal to the longer period. In Wales, the Landlord must let your tenants stay for the notice period and any additional time covered by their final rent payment. If this prescription is not followed, the landlord has not served a valid notice.",
    'tenancyTypeA' : "You have advised us that you are on an Assured Shorthold Tenancy (AST). Section 21 eviction notices cannot be served during an AST unless there is a “break clause” which allows the landlord to prematurely end the AST. If there is a “break clause” in the contract to end the AST,  the notice required in the break clause will first have to be given to the tenant. This will end the AST and transfer the tenancy to a Periodic tenancy. Then the landlord will then have to serve a valid Section 21 notice to evict the tenants. In a sense, for Assured Shorthold Tenancies, at a minimum, two notices are required before a tenant can be evicted. Naturally, there is also the requirement for the Section 21 notice to be valid.",
    'tenancyTypeB' : "If you started on an Assured Shorthold Tenancy (e.g. a one year contract) but stayed on after the fixed-term of the Assured Shorthold Tenancy ended without renewing a new fixed term, you have automatically transferred to a Rolling Tenancy (also known as periodic tenancy). A section 21 notice can be served to tenants on a Rolling Tenancy, but there is still the requirement to follow all the procedures before the Section 21 notice Is considered valid and enforceable.",
    'hmoRuleA' : "You have advised us that the property is an HMO and the property does not have a HMO license. A HMO that does not have a HMO license cannot serve a valid section 21 eviction notice.",
    'hmoRuleB' : "You have advised us that the property is a HMO and you do not know whether the property has a HMO license. A HMO that does not have a HMO license cannot serve a valid section 21 eviction notice. You can check whether the Landlord has a license by contacting the Local Authority (aka Council). Councils generally have a dedicated number for addressing the HMO registration status of a property.",
    'fourMonthsRule' : "You have advised that your tenancy with this landlord commenced within the last 4 months. A Section 21 eviction notice cannot be served within the first 4 months of the tenancy commencing.",
    'energyPerformenceCertificate' : "You have advised us that your landlord has not provided you with an Energy Performance Certificate. A failure to do so renders any subsequent Section 21 eviction notices invalid. If the landlord makes an application to the courts to enforce the eviction, you can advise the court of this point.",
    'howToRentGuide' : "You have advised us that your landlord has not provided you with a HOW TO RENT guide. This guide is an online government document providing advice to current and prospective tenants on the rental process in England and Wales. It details their rights and responsibilities as a tenant, as well as the legal obligations of landlords. Every landlord must ensure their tenant(s) have received a copy of the How to Rent guide at the beginning of their tenancy. A failure to provide this document to tenants renders any subsequent Section 21 notice invalid. "
}
class Section21EvictionAdvice:
    def __init__(self, formData : dict):
        # variable to be passed on to advice template when rendering advice.
        self.title = 'Advice on Private Housing Section 21 (no fault) Evictions.'
        # dict of data collected by Flask from html form
        self.formData = formData
        # data containing advice on eviction
        self.adviceDict = section21EvictionAdviceDict
        # and empty list to which advice will be appended by the class methods
        self.advice = []

    def dataBase(self):
        # retaining limited personal data to see use cases. will be common to all classes
        with open('../database.txt', 'a') as d:
            # variable documenting time at instance call
            time = date.today()
            # variable document name passed to html form
            name = self.formData['User Name'].title()
            # variable documenting the email passed to html form
            email = self.formData['Email'].title()
            # variable documenting post code passed to html form
            postCode = self.formData['Post Code'].upper()
            # variable documenting HTML form additional data field.
            additionalInfo = self.formData['Additional Info'].title()
            # writing the above variables to the txt file named database
            d.write(f"\n{time} :: {name} :: {email} :: {postCode} :: {self.title} :: {additionalInfo}")

    def tenancyType(self):
        if self.formData['Tenancy Type'] == 'Assured Shorthold Tenancy':
            self.advice.append(self.adviceDict['tenancyTypeA'])
            self.advice.append(self.adviceDict['tenancyTypeB'])

    def form6aUsed(self):
        # what to when form6A isn't served.
        if self.formData['Form 6A Given'] == 'No':
            self.advice.append(self.adviceDict['form6aUsed'])

    def depositRequirements(self):
        # what to do if the deposit wasn't protected and the relevant information not given.
        if self.formData['Deposit Amount'] != 0:
            if self.formData['Deposit Protection Scheme Used'] == 'No':
                self.advice.append(self.adviceDict['depositRequirementA'])
        if self.formData['Deposit Amount'] != 0:
            if self.formData['Deposit Protection Notification Given'] == 'No':
                self.advice.append(self.adviceDict['depositRequirementsB'])

    def overChargedDeposit(self):
        # what to do if landlord charged a deposit that's more than 5 weeks rent.
        if self.formData['Deposit Equivalence'] == 'Yes':
            self.advice.append(self.adviceDict['overChargedDeposit'])

    def gasSafetyCertificate(self):
        # advice when gas safety certificate isn't given.
        if self.formData['Gas Safety Certificate Given'] == 'No':
            self.advice.append(self.adviceDict['gasSafetyCertificate'])

    def proscribedInformation(self):
        if self.formData['Proscribe Information Provided'] == 'No':
            self.advice.append(self.adviceDict['proscribedInformation'])

    def energyPerformenceCertificate(self):
        # what to do in the situation the Landlord has not provided the energy performance certificate.
        if self.formData['Energy Performence Certificate Given'] == 'No':
            self.advice.append(self.adviceDict['energyPerformenceCertificate'])

    def howToRentGuide(self):
        # what to do if the landlord has not provided the How to Rent Guide.
        if self.formData['How To Rent Guide Provided'] == 'No':
            self.advice.append(self.adviceDict['howToRentGuide'])

    def fourMonthsRule(self):
        # what to do in the situation the Landlord serves eviction notice within 4 months of the tenancy commencing.
        if self.formData['Moved In 4 Less Than Months Ago'] == 'Yes':
            self.advice.append(self.adviceDict['fourMonthsRule'])

    def hmoRule(self):
        # what to do when a hmo does not have a hmo licence.
        if self.formData['Property A HMO'] == 'Yes':
            if self.formData['HMO Licence Status'] == 'No':
                self.advice.append(self.adviceDict['hmoRuleA'])
            if self.formData['HMO Licence Status'] == "I Don't Know":
                self.advice.append(self.adviceDict['hmoRuleB'])

    def evictionNoticePeriod(self):
        # what to do if the eviction notice gives less than 2 months notice to leave the property.
        if self.formData['Eviction Notice Period'] == 'Less Than 2 Months':
            self.advice.append(self.adviceDict['evictionNoticePeriod'])

    def rentIncrease(self):
        if self.formData['Rent Increase'] == 'Yes':
            if self.formData['New Rent Amount Paid'] == 'Yes':
                self.advice.append("You have advised that you have recently faced a rent increase. Please complete the Rent Increase form to check if the increase was valid. Since you have already started to pay the rent amount, it is unlikely you can challenge the new rent, however you may be able to negotiate with the landlord to have it lowered. Fill out the rent advice form to check your options.")
            elif self.formData['New Rent Amount Paid'] == 'No':
                self.advice.append("You have advised that you have recently faced a rent increase but have not yet paid the new rent amount. Please complete the Rent Advice form to see whether the rent increase is valid and whether you have to pay the new amount.")

    def section8Advice(self):
        # check the section 8 advice
        if self.formData['Behind on Rent'] == 'Yes':
            self.advice.append("Please also complete the Section 8 Eviction Form. Based on the information provided, you may also be facing a Section 8 eviction.")
        elif self.formData['Eviction Type'] == 'Section 8 Eviction Notice':
            self.advice.append("Please also complete the Section 8 Eviction Form. Based on the information provided, you may also be facing a Section 8 eviction.")

    def additionalInfo(self):
        # checks if the user noted anything on the optional form field
        if self.formData['Additional Info']:
            # returns a standard message of we'll get back to you etc.
            self.advice.append(self.adviceDict['additionalInfo'])

    def callMethods(self):
        self.dataBase()
        self.tenancyType()
        self.form6aUsed()
        self.depositRequirements()
        self.overChargedDeposit()
        self.gasSafetyCertificate()
        self.proscribedInformation()
        self.energyPerformenceCertificate()
        self.howToRentGuide()
        self.fourMonthsRule()
        self.hmoRule()
        self.evictionNoticePeriod()
        self.rentIncrease()
        self.section8Advice()
        self.additionalInfo()

section8EvictionAdviceDict = {

}
class Section8EvictionAdvice:
    def __init__(self, formData: dict):
        self.title = 'Advice on Private Housing Section 8 (at fault) Eviction.'
        self.adviceDict = section8EvictionAdviceDict
        self.formData = formData
        self.advice = []

    def rentArrears(self):
        if self.formData['Rent Arrears'] == 'Yes':
            self.advice.append(self.adviceDict['rentArrears'])

    def breachOfTenancy(self):
        if self.formData['Tenancy Breached'] == 'Yes':
            self.advice.append(self.adviceDict['breachOfTenancy'])

    def criminalActivity(self):
        if self.formData['Partook in Criminal Activity'] == 'Yes':
            self.advice.append(self.adviceDict['criminalActivity'])

    def propertyDamage(self):
        if self.formData['Damaged The Property'] == 'Yes':
            self.advice.append(self.adviceDict['propertyDamage'])

    def nuisanceToNeighbours(self):
        if self.formData['Nuisance To Neighbours'] == 'Yes':
            self.advice.append(self.adviceDict['nuisanceToNeighbours'])

    def callMethods(self):
        self.rentArrears()
        self.breachOfTenancy()
        self.criminalActivity()
        self.propertyDamage()
        self.nuisanceToNeighbours()


# link required for form 6A


# ajax crash course  https://www.youtube.com/watch?v=82hnvUYY6QA
# very good explanation on GET & POST methods = https://www.youtube.com/watch?v=SuLBFOHiS5g
# explanation of how to deploy app = https://www.youtube.com/watch?v=AZMQVI6Ss64
# need to learn javascript to auto-submit form data.
# you  can extend multiple templates and do if-elif-else within Flask. If I can figure out how to retrieve data
# automatically I can pass different form templates to the if-elif-else statements.
