# coding: utf-8

from __future__ import absolute_import

# import models into model package
from huaweicloudsdkocr.v1.model.recognize_auto_classification_request import RecognizeAutoClassificationRequest
from huaweicloudsdkocr.v1.model.recognize_auto_classification_request_body import RecognizeAutoClassificationRequestBody
from huaweicloudsdkocr.v1.model.recognize_auto_classification_response import RecognizeAutoClassificationResponse
from huaweicloudsdkocr.v1.model.recognize_auto_classification_result_item_response import RecognizeAutoClassificationResultItemResponse
from huaweicloudsdkocr.v1.model.recognize_bankcard_request import RecognizeBankcardRequest
from huaweicloudsdkocr.v1.model.recognize_bankcard_request_body import RecognizeBankcardRequestBody
from huaweicloudsdkocr.v1.model.recognize_bankcard_response import RecognizeBankcardResponse
from huaweicloudsdkocr.v1.model.recognize_bankcard_result_response import RecognizeBankcardResultResponse
from huaweicloudsdkocr.v1.model.recognize_business_card_items_response import RecognizeBusinessCardItemsResponse
from huaweicloudsdkocr.v1.model.recognize_business_card_request import RecognizeBusinessCardRequest
from huaweicloudsdkocr.v1.model.recognize_business_card_request_body import RecognizeBusinessCardRequestBody
from huaweicloudsdkocr.v1.model.recognize_business_card_response import RecognizeBusinessCardResponse
from huaweicloudsdkocr.v1.model.recognize_business_card_result_response import RecognizeBusinessCardResultResponse
from huaweicloudsdkocr.v1.model.recognize_business_license_request import RecognizeBusinessLicenseRequest
from huaweicloudsdkocr.v1.model.recognize_business_license_request_body import RecognizeBusinessLicenseRequestBody
from huaweicloudsdkocr.v1.model.recognize_business_license_response import RecognizeBusinessLicenseResponse
from huaweicloudsdkocr.v1.model.recognize_business_license_result_response import RecognizeBusinessLicenseResultResponse
from huaweicloudsdkocr.v1.model.recognize_driver_license_request import RecognizeDriverLicenseRequest
from huaweicloudsdkocr.v1.model.recognize_driver_license_request_body import RecognizeDriverLicenseRequestBody
from huaweicloudsdkocr.v1.model.recognize_driver_license_response import RecognizeDriverLicenseResponse
from huaweicloudsdkocr.v1.model.recognize_driver_license_result_response import RecognizeDriverLicenseResultResponse
from huaweicloudsdkocr.v1.model.recognize_financial_statement_request import RecognizeFinancialStatementRequest
from huaweicloudsdkocr.v1.model.recognize_financial_statement_request_body import RecognizeFinancialStatementRequestBody
from huaweicloudsdkocr.v1.model.recognize_financial_statement_response import RecognizeFinancialStatementResponse
from huaweicloudsdkocr.v1.model.recognize_financial_statement_result_response import RecognizeFinancialStatementResultResponse
from huaweicloudsdkocr.v1.model.recognize_financial_statement_words_block_items_response import RecognizeFinancialStatementWordsBlockItemsResponse
from huaweicloudsdkocr.v1.model.recognize_financial_statement_words_list_items_response import RecognizeFinancialStatementWordsListItemsResponse
from huaweicloudsdkocr.v1.model.recognize_financial_statement_words_region_items_response import RecognizeFinancialStatementWordsRegionItemsResponse
from huaweicloudsdkocr.v1.model.recognize_flight_itinerary_items_response import RecognizeFlightItineraryItemsResponse
from huaweicloudsdkocr.v1.model.recognize_flight_itinerary_request import RecognizeFlightItineraryRequest
from huaweicloudsdkocr.v1.model.recognize_flight_itinerary_request_body import RecognizeFlightItineraryRequestBody
from huaweicloudsdkocr.v1.model.recognize_flight_itinerary_response import RecognizeFlightItineraryResponse
from huaweicloudsdkocr.v1.model.recognize_flight_itinerary_result_response import RecognizeFlightItineraryResultResponse
from huaweicloudsdkocr.v1.model.recognize_general_table_items2_response import RecognizeGeneralTableItems2Response
from huaweicloudsdkocr.v1.model.recognize_general_table_items_response import RecognizeGeneralTableItemsResponse
from huaweicloudsdkocr.v1.model.recognize_general_table_request import RecognizeGeneralTableRequest
from huaweicloudsdkocr.v1.model.recognize_general_table_request_body import RecognizeGeneralTableRequestBody
from huaweicloudsdkocr.v1.model.recognize_general_table_response import RecognizeGeneralTableResponse
from huaweicloudsdkocr.v1.model.recognize_general_table_result_response import RecognizeGeneralTableResultResponse
from huaweicloudsdkocr.v1.model.recognize_general_text_items_response import RecognizeGeneralTextItemsResponse
from huaweicloudsdkocr.v1.model.recognize_general_text_request import RecognizeGeneralTextRequest
from huaweicloudsdkocr.v1.model.recognize_general_text_request_body import RecognizeGeneralTextRequestBody
from huaweicloudsdkocr.v1.model.recognize_general_text_response import RecognizeGeneralTextResponse
from huaweicloudsdkocr.v1.model.recognize_general_text_result_response import RecognizeGeneralTextResultResponse
from huaweicloudsdkocr.v1.model.recognize_handwriting_items_response import RecognizeHandwritingItemsResponse
from huaweicloudsdkocr.v1.model.recognize_handwriting_request import RecognizeHandwritingRequest
from huaweicloudsdkocr.v1.model.recognize_handwriting_request_body import RecognizeHandwritingRequestBody
from huaweicloudsdkocr.v1.model.recognize_handwriting_response import RecognizeHandwritingResponse
from huaweicloudsdkocr.v1.model.recognize_handwriting_result_response import RecognizeHandwritingResultResponse
from huaweicloudsdkocr.v1.model.recognize_id_card_request import RecognizeIdCardRequest
from huaweicloudsdkocr.v1.model.recognize_id_card_request_body import RecognizeIdCardRequestBody
from huaweicloudsdkocr.v1.model.recognize_id_card_response import RecognizeIdCardResponse
from huaweicloudsdkocr.v1.model.recognize_id_card_result_response import RecognizeIdCardResultResponse
from huaweicloudsdkocr.v1.model.recognize_license_plate_request import RecognizeLicensePlateRequest
from huaweicloudsdkocr.v1.model.recognize_license_plate_request_body import RecognizeLicensePlateRequestBody
from huaweicloudsdkocr.v1.model.recognize_license_plate_response import RecognizeLicensePlateResponse
from huaweicloudsdkocr.v1.model.recognize_license_plate_result_items_response import RecognizeLicensePlateResultItemsResponse
from huaweicloudsdkocr.v1.model.recognize_mvs_invoice_request import RecognizeMvsInvoiceRequest
from huaweicloudsdkocr.v1.model.recognize_mvs_invoice_request_body import RecognizeMvsInvoiceRequestBody
from huaweicloudsdkocr.v1.model.recognize_mvs_invoice_response import RecognizeMvsInvoiceResponse
from huaweicloudsdkocr.v1.model.recognize_mvs_invoice_result_response import RecognizeMvsInvoiceResultResponse
from huaweicloudsdkocr.v1.model.recognize_passport_request import RecognizePassportRequest
from huaweicloudsdkocr.v1.model.recognize_passport_request_body import RecognizePassportRequestBody
from huaweicloudsdkocr.v1.model.recognize_passport_response import RecognizePassportResponse
from huaweicloudsdkocr.v1.model.recognize_passport_result_response import RecognizePassportResultResponse
from huaweicloudsdkocr.v1.model.recognize_quota_invoice_request import RecognizeQuotaInvoiceRequest
from huaweicloudsdkocr.v1.model.recognize_quota_invoice_request_body import RecognizeQuotaInvoiceRequestBody
from huaweicloudsdkocr.v1.model.recognize_quota_invoice_response import RecognizeQuotaInvoiceResponse
from huaweicloudsdkocr.v1.model.recognize_quota_invoice_result_response import RecognizeQuotaInvoiceResultResponse
from huaweicloudsdkocr.v1.model.recognize_taxi_invoice_request import RecognizeTaxiInvoiceRequest
from huaweicloudsdkocr.v1.model.recognize_taxi_invoice_request_body import RecognizeTaxiInvoiceRequestBody
from huaweicloudsdkocr.v1.model.recognize_taxi_invoice_response import RecognizeTaxiInvoiceResponse
from huaweicloudsdkocr.v1.model.recognize_taxi_invoice_result_response import RecognizeTaxiInvoiceResultResponse
from huaweicloudsdkocr.v1.model.recognize_toll_invoice_request import RecognizeTollInvoiceRequest
from huaweicloudsdkocr.v1.model.recognize_toll_invoice_request_body import RecognizeTollInvoiceRequestBody
from huaweicloudsdkocr.v1.model.recognize_toll_invoice_response import RecognizeTollInvoiceResponse
from huaweicloudsdkocr.v1.model.recognize_toll_invoice_result_response import RecognizeTollInvoiceResultResponse
from huaweicloudsdkocr.v1.model.recognize_train_ticket_request import RecognizeTrainTicketRequest
from huaweicloudsdkocr.v1.model.recognize_train_ticket_request_body import RecognizeTrainTicketRequestBody
from huaweicloudsdkocr.v1.model.recognize_train_ticket_response import RecognizeTrainTicketResponse
from huaweicloudsdkocr.v1.model.recognize_train_ticket_result_response import RecognizeTrainTicketResultResponse
from huaweicloudsdkocr.v1.model.recognize_transportation_license_request import RecognizeTransportationLicenseRequest
from huaweicloudsdkocr.v1.model.recognize_transportation_license_request_body import RecognizeTransportationLicenseRequestBody
from huaweicloudsdkocr.v1.model.recognize_transportation_license_response import RecognizeTransportationLicenseResponse
from huaweicloudsdkocr.v1.model.recognize_transportation_license_result_response import RecognizeTransportationLicenseResultResponse
from huaweicloudsdkocr.v1.model.recognize_vat_invoice_items_response import RecognizeVatInvoiceItemsResponse
from huaweicloudsdkocr.v1.model.recognize_vat_invoice_request import RecognizeVatInvoiceRequest
from huaweicloudsdkocr.v1.model.recognize_vat_invoice_request_body import RecognizeVatInvoiceRequestBody
from huaweicloudsdkocr.v1.model.recognize_vat_invoice_response import RecognizeVatInvoiceResponse
from huaweicloudsdkocr.v1.model.recognize_vat_invoice_result_response import RecognizeVatInvoiceResultResponse
from huaweicloudsdkocr.v1.model.recognize_vehicle_license_request import RecognizeVehicleLicenseRequest
from huaweicloudsdkocr.v1.model.recognize_vehicle_license_request_body import RecognizeVehicleLicenseRequestBody
from huaweicloudsdkocr.v1.model.recognize_vehicle_license_response import RecognizeVehicleLicenseResponse
from huaweicloudsdkocr.v1.model.recognize_vehicle_license_result_response import RecognizeVehicleLicenseResultResponse
from huaweicloudsdkocr.v1.model.recognize_vin_request import RecognizeVinRequest
from huaweicloudsdkocr.v1.model.recognize_vin_request_body import RecognizeVinRequestBody
from huaweicloudsdkocr.v1.model.recognize_vin_response import RecognizeVinResponse
from huaweicloudsdkocr.v1.model.recognize_vin_result_response import RecognizeVinResultResponse
from huaweicloudsdkocr.v1.model.recognize_web_image_items_response import RecognizeWebImageItemsResponse
from huaweicloudsdkocr.v1.model.recognize_web_image_request import RecognizeWebImageRequest
from huaweicloudsdkocr.v1.model.recognize_web_image_request_body import RecognizeWebImageRequestBody
from huaweicloudsdkocr.v1.model.recognize_web_image_response import RecognizeWebImageResponse
from huaweicloudsdkocr.v1.model.recognize_web_image_result_response import RecognizeWebImageResultResponse
