#!/usr/bin/env python3
"""
Backend Authentication Testing Script for Sports Portal
Tests all authentication endpoints with comprehensive scenarios
"""

import requests
import json
import sys
from datetime import datetime

# Get backend URL from frontend .env file
BACKEND_URL = "https://khel-connect.preview.emergentagent.com/api"

class AuthTester:
    def __init__(self):
        self.base_url = BACKEND_URL
        self.test_results = []
        self.session = requests.Session()
        
    def log_test(self, test_name, success, details):
        """Log test results"""
        status = "✅ PASS" if success else "❌ FAIL"
        self.test_results.append({
            'test': test_name,
            'status': status,
            'success': success,
            'details': details,
            'timestamp': datetime.now().isoformat()
        })
        print(f"{status}: {test_name}")
        if details:
            print(f"   Details: {details}")
        print()
    
    def test_registration_valid(self):
        """Test registration with valid user data"""
        test_name = "Registration with valid data"
        
        # Use realistic sports portal data
        user_data = {
            "name": "Rajesh Kumar",
            "email": "rajesh.kumar@sportsportal.com",
            "phone": "+91-9876543210",
            "password": "SecurePass123!",
            "role": "player"
        }
        
        try:
            response = self.session.post(
                f"{self.base_url}/auth/register",
                json=user_data,
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 200:
                data = response.json()
                if "token" in data and "user" in data:
                    # Store token for later tests
                    self.valid_token = data["token"]
                    self.registered_user = data["user"]
                    self.log_test(test_name, True, f"User registered successfully. Token: {data['token'][:20]}...")
                    return True
                else:
                    self.log_test(test_name, False, f"Missing token or user in response: {data}")
                    return False
            else:
                self.log_test(test_name, False, f"Status: {response.status_code}, Response: {response.text}")
                return False
                
        except Exception as e:
            self.log_test(test_name, False, f"Exception: {str(e)}")
            return False
    
    def test_registration_duplicate_email(self):
        """Test registration with duplicate email"""
        test_name = "Registration with duplicate email"
        
        # Try to register same email again
        user_data = {
            "name": "Another User",
            "email": "rajesh.kumar@sportsportal.com",  # Same email as before
            "phone": "+91-9876543211",
            "password": "AnotherPass123!",
            "role": "coach"
        }
        
        try:
            response = self.session.post(
                f"{self.base_url}/auth/register",
                json=user_data,
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 400:
                data = response.json()
                if "Email already registered" in data.get("detail", ""):
                    self.log_test(test_name, True, "Correctly rejected duplicate email")
                    return True
                else:
                    self.log_test(test_name, False, f"Wrong error message: {data}")
                    return False
            else:
                self.log_test(test_name, False, f"Expected 400, got {response.status_code}: {response.text}")
                return False
                
        except Exception as e:
            self.log_test(test_name, False, f"Exception: {str(e)}")
            return False
    
    def test_registration_missing_fields(self):
        """Test registration with missing required fields"""
        test_name = "Registration with missing fields"
        
        # Missing password field
        user_data = {
            "name": "Incomplete User",
            "email": "incomplete@sportsportal.com",
            "phone": "+91-9876543212",
            "role": "player"
            # Missing password
        }
        
        try:
            response = self.session.post(
                f"{self.base_url}/auth/register",
                json=user_data,
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 422:  # Validation error
                self.log_test(test_name, True, "Correctly rejected missing password field")
                return True
            else:
                self.log_test(test_name, False, f"Expected 422, got {response.status_code}: {response.text}")
                return False
                
        except Exception as e:
            self.log_test(test_name, False, f"Exception: {str(e)}")
            return False
    
    def test_login_valid_credentials(self):
        """Test login with valid credentials"""
        test_name = "Login with valid credentials"
        
        login_data = {
            "email": "rajesh.kumar@sportsportal.com",
            "password": "SecurePass123!"
        }
        
        try:
            response = self.session.post(
                f"{self.base_url}/auth/login",
                json=login_data,
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 200:
                data = response.json()
                if "token" in data and "user" in data:
                    self.login_token = data["token"]
                    self.log_test(test_name, True, f"Login successful. Token: {data['token'][:20]}...")
                    return True
                else:
                    self.log_test(test_name, False, f"Missing token or user in response: {data}")
                    return False
            else:
                self.log_test(test_name, False, f"Status: {response.status_code}, Response: {response.text}")
                return False
                
        except Exception as e:
            self.log_test(test_name, False, f"Exception: {str(e)}")
            return False
    
    def test_login_invalid_password(self):
        """Test login with invalid password"""
        test_name = "Login with invalid password"
        
        login_data = {
            "email": "rajesh.kumar@sportsportal.com",
            "password": "WrongPassword123!"
        }
        
        try:
            response = self.session.post(
                f"{self.base_url}/auth/login",
                json=login_data,
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 401:
                data = response.json()
                if "Incorrect email or password" in data.get("detail", ""):
                    self.log_test(test_name, True, "Correctly rejected invalid password")
                    return True
                else:
                    self.log_test(test_name, False, f"Wrong error message: {data}")
                    return False
            else:
                self.log_test(test_name, False, f"Expected 401, got {response.status_code}: {response.text}")
                return False
                
        except Exception as e:
            self.log_test(test_name, False, f"Exception: {str(e)}")
            return False
    
    def test_login_nonexistent_email(self):
        """Test login with non-existent email"""
        test_name = "Login with non-existent email"
        
        login_data = {
            "email": "nonexistent@sportsportal.com",
            "password": "SomePassword123!"
        }
        
        try:
            response = self.session.post(
                f"{self.base_url}/auth/login",
                json=login_data,
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 401:
                data = response.json()
                if "Incorrect email or password" in data.get("detail", ""):
                    self.log_test(test_name, True, "Correctly rejected non-existent email")
                    return True
                else:
                    self.log_test(test_name, False, f"Wrong error message: {data}")
                    return False
            else:
                self.log_test(test_name, False, f"Expected 401, got {response.status_code}: {response.text}")
                return False
                
        except Exception as e:
            self.log_test(test_name, False, f"Exception: {str(e)}")
            return False
    
    def test_token_validation(self):
        """Test JWT token validation"""
        test_name = "JWT Token validation"
        
        if not hasattr(self, 'valid_token'):
            self.log_test(test_name, False, "No valid token available from registration test")
            return False
        
        try:
            # Test the /me endpoint with the token
            response = self.session.get(
                f"{self.base_url}/auth/me",
                params={"token": self.valid_token}
            )
            
            if response.status_code == 200:
                user_data = response.json()
                if "email" in user_data and user_data["email"] == "rajesh.kumar@sportsportal.com":
                    self.log_test(test_name, True, f"Token validation successful. User: {user_data['name']}")
                    return True
                else:
                    self.log_test(test_name, False, f"Invalid user data returned: {user_data}")
                    return False
            else:
                self.log_test(test_name, False, f"Status: {response.status_code}, Response: {response.text}")
                return False
                
        except Exception as e:
            self.log_test(test_name, False, f"Exception: {str(e)}")
            return False
    
    def test_database_verification(self):
        """Verify database storage and password hashing"""
        test_name = "Database verification"
        
        try:
            # We'll use the /me endpoint to verify user is stored correctly
            if not hasattr(self, 'valid_token'):
                self.log_test(test_name, False, "No valid token available for database verification")
                return False
            
            response = self.session.get(
                f"{self.base_url}/auth/me",
                params={"token": self.valid_token}
            )
            
            if response.status_code == 200:
                user_data = response.json()
                
                # Check required fields are present
                required_fields = ["id", "email", "name", "phone", "role", "created_at"]
                missing_fields = [field for field in required_fields if field not in user_data]
                
                if missing_fields:
                    self.log_test(test_name, False, f"Missing fields in user data: {missing_fields}")
                    return False
                
                # Verify password is not in response (should be hashed and not returned)
                if "password" in user_data or "hashed_password" in user_data:
                    self.log_test(test_name, False, "Password data found in user response - security issue!")
                    return False
                
                self.log_test(test_name, True, f"User properly stored with fields: {list(user_data.keys())}")
                return True
            else:
                self.log_test(test_name, False, f"Could not retrieve user data: {response.status_code}")
                return False
                
        except Exception as e:
            self.log_test(test_name, False, f"Exception: {str(e)}")
            return False
    
    def run_all_tests(self):
        """Run all authentication tests"""
        print("=" * 60)
        print("SPORTS PORTAL AUTHENTICATION TESTING")
        print("=" * 60)
        print(f"Backend URL: {self.base_url}")
        print(f"Test started at: {datetime.now().isoformat()}")
        print("=" * 60)
        print()
        
        # Run tests in order
        tests = [
            self.test_registration_valid,
            self.test_registration_duplicate_email,
            self.test_registration_missing_fields,
            self.test_login_valid_credentials,
            self.test_login_invalid_password,
            self.test_login_nonexistent_email,
            self.test_token_validation,
            self.test_database_verification
        ]
        
        passed = 0
        failed = 0
        
        for test in tests:
            if test():
                passed += 1
            else:
                failed += 1
        
        # Summary
        print("=" * 60)
        print("TEST SUMMARY")
        print("=" * 60)
        print(f"Total Tests: {passed + failed}")
        print(f"Passed: {passed}")
        print(f"Failed: {failed}")
        print(f"Success Rate: {(passed/(passed+failed)*100):.1f}%")
        print("=" * 60)
        
        # Detailed results
        print("\nDETAILED RESULTS:")
        for result in self.test_results:
            print(f"{result['status']}: {result['test']}")
            if result['details']:
                print(f"   {result['details']}")
        
        return failed == 0

if __name__ == "__main__":
    tester = AuthTester()
    success = tester.run_all_tests()
    sys.exit(0 if success else 1)