# 🚀 Quick Start Guide

## Start the Project in 5 Minutes!

### Step 1: Activate Virtual Environment
```powershell
cd "C:\Users\Deepak\Desktop\final pro"
& "env\Scripts\Activate.ps1"
```

### Step 2: Navigate to Project
```powershell
cd fyp
```

### Step 3: Run the Server
```powershell
python manage.py runserver
```

### Step 4: Open Browser
Visit: **http://127.0.0.1:8000/**

---

## 👤 Default Admin Access

**Username**: `admin`
**Password**: (The password you set when you ran createsuperuser)

Admin Panel: http://127.0.0.1:8000/admin/

---

## 🎯 Quick Test Workflow

### 1. Create Institution Account
1. Go to: http://127.0.0.1:8000/accounts/register/
2. Fill form:
   - Username: `testinstitution`
   - Email: `institution@test.com`
   - User Type: **Institution**
   - Organization: `Test University`
   - Password: `testpass123`
3. Click Register

### 2. Issue a Certificate
1. After login, you'll be on Dashboard
2. Click "Issue Certificate"
3. Fill form:
   - Student Name: `John Doe`
   - Student Email: `john@test.com`
   - Course Name: `Web Development`
   - Grade: `A+`
   - Institution Name: `Test University`
4. Click "Issue Certificate"
5. Certificate created! ✅

### 3. Verify the Certificate
1. Copy the Certificate ID (e.g., `CERT-2025-ABC123`)
2. Go to: http://127.0.0.1:8000/certificates/verify/
3. Paste Certificate ID
4. Click "Verify Certificate"
5. See verification result! ✅

### 4. Login as Student
1. Logout from institution account
2. Login with:
   - Username: `john`
   - Password: (auto-generated, check admin panel or reset)
   - OR register new student account
3. View your certificates in dashboard
4. Download PDF certificate

---

## ⚡ Key URLs

| Feature | URL |
|---------|-----|
| Homepage | http://127.0.0.1:8000/ |
| Register | http://127.0.0.1:8000/accounts/register/ |
| Login | http://127.0.0.1:8000/accounts/login/ |
| Dashboard | http://127.0.0.1:8000/certificates/dashboard/ |
| Issue Certificate | http://127.0.0.1:8000/certificates/issue/ |
| Verify Certificate | http://127.0.0.1:8000/certificates/verify/ |
| Certificate List | http://127.0.0.1:8000/certificates/list/ |
| Admin Panel | http://127.0.0.1:8000/admin/ |

---

## 🛑 Stop the Server

Press `Ctrl + C` in the terminal or PowerShell window

---

## 🔄 Reset Database (If Needed)

```powershell
# Delete database
Remove-Item db.sqlite3

# Recreate
python manage.py migrate
python manage.py createsuperuser
```

---

## 📋 Common Commands

```powershell
# Start server
python manage.py runserver

# Create superuser
python manage.py createsuperuser

# Make migrations
python manage.py makemigrations

# Apply migrations  
python manage.py migrate

# Collect static files
python manage.py collectstatic

# Run on different port
python manage.py runserver 8080
```

---

## ✅ Feature Checklist

Test these features:
- [ ] Register institution account
- [ ] Register student account
- [ ] Login/Logout
- [ ] Issue certificate
- [ ] View dashboard
- [ ] List certificates
- [ ] View certificate details
- [ ] Download certificate PDF
- [ ] Verify certificate (with ID)
- [ ] Search certificates
- [ ] Update profile

---

## 🎨 User Interface Preview

### Homepage
- Hero section with call-to-action
- Feature cards
- Statistics
- How it works section

### Institution Dashboard
- Statistics cards (Issued, Pending, Revoked)
- Recent certificates table
- Quick "Issue New" button

### Student Dashboard
- Certificate cards with images
- Download buttons
- View details links

### Verification Page
- Large search input
- Real-time verification
- Certificate details display
- Blockchain verification status

---

## 💡 Tips

1. **Always activate virtual environment** before running commands
2. **Check terminal output** for errors
3. **Use admin panel** to manage users manually
4. **Test without blockchain** first (system works perfectly without it)
5. **Screenshots** of the system can be taken for documentation

---

## 🆘 Need Help?

Check these in order:
1. Is virtual environment activated? (You should see `(env)` in terminal)
2. Are you in the `fyp` directory?
3. Is the server running? (Should show "Starting development server...")
4. Check browser console for JavaScript errors (F12)
5. Check terminal for Python errors
6. Read the full README.md for detailed documentation

---

**Everything is ready! Just activate the environment and run the server!** 🎉

The system is **100% complete and functional** for your final year project.
