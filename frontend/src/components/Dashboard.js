import React, { useState } from 'react';
import { useAuth } from '../context/AuthContext';
import { useNavigate } from 'react-router-dom';
import { Button } from './ui/button';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './ui/card';
import { User, FileText, Calendar, Award, MapPin, Building2, LogOut, Menu, X } from 'lucide-react';

const Dashboard = () => {
  const { user, logout } = useAuth();
  const navigate = useNavigate();
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  const services = [
    {
      title: 'Player Registration',
      description: 'For Financial Aid, Direct Recruitment, and Awards',
      icon: <User className="h-12 w-12 text-[#7B1E4D]" />,
      link: '#'
    },
    {
      title: 'Facility Booking',
      description: 'For Stadiums, Guest Houses, Gyms & Swimming Pools',
      icon: <Building2 className="h-12 w-12 text-green-600" />,
      link: '#'
    },
    {
      title: 'Sports Calendar',
      description: 'For Coaching Camps & Sports Competitions',
      icon: <Calendar className="h-12 w-12 text-orange-600" />,
      link: '#'
    },
    {
      title: 'Tournament Registration',
      description: 'Register for upcoming cricket tournaments',
      icon: <Award className="h-12 w-12 text-blue-600" />,
      link: '#'
    },
    {
      title: 'Venue Locator',
      description: 'Find cricket grounds and facilities near you',
      icon: <MapPin className="h-12 w-12 text-red-600" />,
      link: '#'
    },
    {
      title: 'Certificates',
      description: 'Download your participation and achievement certificates',
      icon: <FileText className="h-12 w-12 text-purple-600" />,
      link: '#'
    }
  ];

  const officials = [
    {
      name: 'Rajesh Kumar',
      position: 'President',
      organization: 'Tennis Ball Cricket Association',
      image: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=200&h=200&fit=crop'
    },
    {
      name: 'Priya Sharma',
      position: 'Secretary',
      organization: 'TBCAI',
      image: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=200&h=200&fit=crop'
    },
    {
      name: 'Amit Patel',
      position: 'Treasurer',
      organization: 'TBCAI',
      image: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=200&h=200&fit=crop'
    },
    {
      name: 'Dr. Sandeep Singh',
      position: 'Director',
      organization: 'Sports Development',
      image: 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=200&h=200&fit=crop'
    }
  ];

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow-md sticky top-0 z-50">
        <div className="container mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-4">
              <img 
                src="https://customer-assets.emergentagent.com/job_dff33f85-1f1c-4271-ac8f-64c6077e9ef3/artifacts/504uzyb1_WhatsApp%20Image%202025-12-31%20at%2006.50.29.jpeg" 
                alt="TBCAI Logo" 
                className="h-16 w-16 object-contain"
              />
              <div>
                <h1 className="text-2xl font-bold text-[#7B1E4D]">SPORTS PORTAL</h1>
                <p className="text-sm text-gray-600">Tennis Ball Cricket Association of India</p>
              </div>
            </div>
            
            {/* Desktop Menu */}
            <div className="hidden md:flex items-center space-x-4">
              <div className="text-right">
                <p className="text-sm font-semibold text-gray-700">{user?.name}</p>
                <p className="text-xs text-gray-500 capitalize">{user?.role}</p>
              </div>
              <Button 
                onClick={handleLogout}
                variant="outline"
                className="border-[#7B1E4D] text-[#7B1E4D] hover:bg-[#7B1E4D] hover:text-white"
              >
                <LogOut className="h-4 w-4 mr-2" />
                Logout
              </Button>
            </div>

            {/* Mobile Menu Button */}
            <button 
              className="md:hidden"
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            >
              {mobileMenuOpen ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
            </button>
          </div>

          {/* Mobile Menu */}
          {mobileMenuOpen && (
            <div className="md:hidden mt-4 py-4 border-t">
              <div className="space-y-3">
                <p className="font-semibold text-gray-700">{user?.name}</p>
                <p className="text-sm text-gray-500 capitalize">{user?.role}</p>
                <Button 
                  onClick={handleLogout}
                  variant="outline"
                  className="w-full border-[#7B1E4D] text-[#7B1E4D]"
                >
                  <LogOut className="h-4 w-4 mr-2" />
                  Logout
                </Button>
              </div>
            </div>
          )}
        </div>
      </header>

      {/* Hero Banner */}
      <div className="relative bg-gradient-to-r from-[#7B1E4D] to-[#621839] text-white py-16">
        <div className="absolute inset-0 overflow-hidden">
          <div className="absolute -top-10 -right-10 w-64 h-64 bg-purple-500 opacity-20 rounded-full"></div>
          <div className="absolute top-20 -left-10 w-40 h-40 bg-orange-500 opacity-20 rounded-full"></div>
        </div>
        <div className="container mx-auto px-4 relative z-10">
          <h2 className="text-4xl md:text-5xl font-bold mb-4">Welcome to Sports Portal</h2>
          <p className="text-lg md:text-xl max-w-2xl">Register, compete, and excel in tennis ball cricket tournaments across India. Join thousands of players in the most exciting cricket community.</p>
        </div>
      </div>

      {/* Services Section */}
      <section className="container mx-auto px-4 py-12">
        <h2 className="text-3xl font-bold text-center mb-8 text-[#7B1E4D]">Online Services</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {services.map((service, index) => (
            <Card 
              key={index} 
              className="hover:shadow-xl transition-shadow duration-300 cursor-pointer border-t-4 border-[#7B1E4D]"
            >
              <CardHeader className="text-center">
                <div className="flex justify-center mb-4">
                  {service.icon}
                </div>
                <CardTitle className="text-lg">{service.title}</CardTitle>
                <CardDescription>{service.description}</CardDescription>
              </CardHeader>
              <CardContent className="text-center">
                <Button 
                  className="bg-[#7B1E4D] hover:bg-[#621839] text-white"
                  onClick={() => console.log('Service clicked:', service.title)}
                >
                  Access Service
                </Button>
              </CardContent>
            </Card>
          ))}
        </div>
      </section>

      {/* Officials Section */}
      <section className="bg-white py-12">
        <div className="container mx-auto px-4">
          <h2 className="text-3xl font-bold text-center mb-8 text-[#7B1E4D]">Our Officials</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            {officials.map((official, index) => (
              <Card key={index} className="text-center hover:shadow-lg transition-shadow">
                <CardHeader>
                  <div className="flex justify-center mb-4">
                    <img 
                      src={official.image} 
                      alt={official.name}
                      className="w-24 h-24 rounded-full object-cover border-4 border-[#7B1E4D]"
                    />
                  </div>
                  <CardTitle className="text-lg text-[#7B1E4D]">{official.name}</CardTitle>
                  <CardDescription>
                    <p className="font-semibold">{official.position}</p>
                    <p className="text-sm">{official.organization}</p>
                  </CardDescription>
                </CardHeader>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* Mission Section */}
      <section className="container mx-auto px-4 py-12">
        <Card className="bg-gradient-to-r from-purple-50 to-pink-50 border-none">
          <CardHeader>
            <CardTitle className="text-3xl font-bold text-center text-[#7B1E4D]">
              State Initiative for <span className="text-orange-600">Development of Sports</span>
            </CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-center text-gray-700 max-w-4xl mx-auto leading-relaxed">
              The importance of sports and fitness in one's life is invaluable. Playing sports inculcates team spirit, 
              develops strategic & analytical thinking, leadership skills, goal setting and risk taking. 
              A fit and healthy individual leads to an equally healthy society and strong nation.
            </p>
          </CardContent>
        </Card>
      </section>

      {/* Footer */}
      <footer className="bg-[#7B1E4D] text-white py-8">
        <div className="container mx-auto px-4">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div>
              <h3 className="font-bold text-lg mb-4">Quick Links</h3>
              <ul className="space-y-2 text-sm">
                <li><a href="#" className="hover:text-orange-300">About Us</a></li>
                <li><a href="#" className="hover:text-orange-300">Contact</a></li>
                <li><a href="#" className="hover:text-orange-300">Rules & Regulations</a></li>
                <li><a href="#" className="hover:text-orange-300">FAQ</a></li>
              </ul>
            </div>
            <div>
              <h3 className="font-bold text-lg mb-4">Services</h3>
              <ul className="space-y-2 text-sm">
                <li><a href="#" className="hover:text-orange-300">Player Registration</a></li>
                <li><a href="#" className="hover:text-orange-300">Tournament Schedule</a></li>
                <li><a href="#" className="hover:text-orange-300">Venue Booking</a></li>
                <li><a href="#" className="hover:text-orange-300">Results</a></li>
              </ul>
            </div>
            <div>
              <h3 className="font-bold text-lg mb-4">Contact Info</h3>
              <p className="text-sm leading-relaxed">
                Tennis Ball Cricket Association of India<br />
                Email: info@tbcai.in<br />
                Phone: +91 123 456 7890
              </p>
            </div>
          </div>
          <div className="border-t border-white/20 mt-8 pt-6 text-center text-sm">
            <p>&copy; 2025 Tennis Ball Cricket Association of India. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default Dashboard;
